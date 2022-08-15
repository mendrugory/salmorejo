from kubernetes import client, watch
from k8s import Watcher

_deployment_watcher = None

def get_deployment_watcher(namespace=None):
    global _deployment_watcher
    if _deployment_watcher is None:
        _deployment_watcher = DeploymentWatcher(namespace=namespace)
    return _deployment_watcher

class DeploymentWatcher(Watcher):
    def __init__(self, namespace=None, auto_start=False):
        self.namespace=namespace
        super().__init__(auto_start)

    def get_stream_args(self):
        if self.namespace is None:
            return [client.AppsV1Api().list_deployment_for_all_namespaces]
            
        return [client.AppsV1Api().list_namespaced_deployment,\
                self.namespace]
                
    def get_stream_kwargs(self):
        return self._get_stream_default_kwargs()
