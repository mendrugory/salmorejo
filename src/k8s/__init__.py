import re
import time
from http import HTTPStatus
from ssl import SSLError
from urllib3.exceptions import MaxRetryError
from threading import Thread
import kubernetes
from config.logger import get_logger

_DEFAULT_TIMEOUT=60
_DEFAULT_WAITING_TIME_AFTER_NET_ERROR=3
_INITIAL_RESOURCE_VERSION=None
_REGEX_NEWER_RESOURCE_VERSION = '^.+\((\d+)\)$'
_REGEX_NEWER_RESOURCE_VERSION_POSITION = 1

logger = get_logger()

def load_kubeconfig():
    kubernetes.config.load_kube_config()

class Watcher(Thread):
    def __init__(self, auto_start=False):
        super().__init__()
        self.observers = list()
        self.resource_version = _INITIAL_RESOURCE_VERSION
        self.waiting_time_after_net_error = _DEFAULT_WAITING_TIME_AFTER_NET_ERROR
        self.timeout = _DEFAULT_TIMEOUT
        if auto_start:
            self.start()

    def _get_stream_default_kwargs(self):
        return dict(
            resource_version=self.resource_version,
            _request_timeout=self.timeout
        )

    def _notify(self, event):
        for o in self.observers:
            o.notify(event)

    def register(self, observer):
        self.observers.append(observer)

    def run(self):    
        while True:
            try:
                self._stream()
            except SSLError as e:
                if e.args and 'timed out' in e.args:
                    logger.debug(f'Timed out watcher loop: {e}')
                else:
                    logger.debug(f'SSLError watcher loop: {e}')
            except kubernetes.client.rest.ApiException as e:
                logger.debug(f'Watcher loop ApiException: {e}')
                if e.status == HTTPStatus.GONE:
                    newer_resource_version = Watcher._get_resource_version_from_exception(e.reason)
                    self._update_resource_version(new_resource_version=newer_resource_version)
            except MaxRetryError as e:
                logger.debug(f"watcher loop MaxRetryError {e}")
                time.sleep(_DEFAULT_WAITING_TIME_AFTER_NET_ERROR)
            except Exception as e:
                logger.debug(f"watcher loop Exception {e}")

    @staticmethod
    def _get_resource_version_from_exception(reason):
        match = re.match(_REGEX_NEWER_RESOURCE_VERSION, reason)
        if match and match.group(_REGEX_NEWER_RESOURCE_VERSION_POSITION):
            return int(match.group(_REGEX_NEWER_RESOURCE_VERSION_POSITION))
        return None

    def _stream(self):
        args = self.get_stream_args()
        kwargs = self.get_stream_kwargs()
        for event in kubernetes.watch.Watch().stream(*args, **kwargs):
            self._update_resource_version(obj=event)
            self._notify(event)

    def _update_resource_version(self, obj=None, new_resource_version=None):
        if new_resource_version:
            self.resource_version = new_resource_version
            return
        
        if obj:
            k8s_object = obj['object'] if 'object' in obj else obj
            self.resource_version = int(k8s_object.metadata.resource_version)
