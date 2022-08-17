from kubernetes import client
from k8s import Watcher

_ingress_watcher = None

def get_ingress_watcher(namespace=None):
    global _ingress_watcher
    if _ingress_watcher is None:
        _ingress_watcher = IngressWatcher(namespace=namespace)
    return _ingress_watcher


class IngressWatcher(Watcher):
    def __init__(self, namespace=None, auto_start=False):
        self.namespace=namespace
        super().__init__(auto_start)

    def get_stream_args(self):
        if self.namespace is None:
            return [client.NetworkingV1Api().list_ingress_for_all_namespaces]
            
        return [client.NetworkingV1Api().list_namespaced_ingress, self.namespace]

    def get_stream_kwargs(self):
        return self._get_stream_default_kwargs()  
