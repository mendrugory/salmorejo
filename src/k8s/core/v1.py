from kubernetes import client
from k8s import Watcher

_pod_watcher = None
_service_watcher = None

def get_pod_watcher(namespace=None):
    global _pod_watcher
    if _pod_watcher is None:
        _pod_watcher = PodWatcher(namespace=namespace)
    return _pod_watcher

def get_service_watcher(namespace=None):
    global _service_watcher
    if _service_watcher is None:
        _service_watcher = ServiceWatcher(namespace=namespace)
    return _service_watcher    

class PodWatcher(Watcher):
    def __init__(self, namespace=None, auto_start=False):
        self.namespace=namespace
        super().__init__(auto_start)

    def get_stream_args(self):
        if self.namespace is None:
            return [client.CoreV1Api().list_pod_for_all_namespaces]
            
        return [client.CoreV1Api().list_namespaced_pod, self.namespace]

    def get_stream_kwargs(self):
        return self._get_stream_default_kwargs()    

class ServiceWatcher(Watcher):
    def __init__(self, namespace=None, auto_start=False):
        self.namespace=namespace
        super().__init__(auto_start)
    
    def get_stream_args(self):
        if self.namespace is None:
            return [client.CoreV1Api().list_service_for_all_namespaces]
            
        return [client.CoreV1Api().list_namespaced_service, self.namespace]
                

    def get_stream_kwargs(self):
        return self._get_stream_default_kwargs()        