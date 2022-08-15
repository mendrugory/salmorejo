import logging
from k8s import load_kubeconfig
from k8s.watcher import get_watcher
from config.logger import get_logger

logger = get_logger()

class Manager():
    def __init__(self, callback, k8s_objects):
        self.service  = Service(callback)
        self.watchers = set(get_watcher(o) for o in k8s_objects)

    def start(self):
        logger.debug(f"There is {len(self.watchers)} watchers.")
        load_kubeconfig()
        for w in self.watchers:
            w.register(self.service)
            w.start()
        for w in self.watchers:
            w.join()

class Service():
    def __init__(self, callback):
        self.callback = callback

    def notify(self, event):
        try:
            self.callback(event)
        except Exception as e:
            logger.error(f"callback error: {e}")
