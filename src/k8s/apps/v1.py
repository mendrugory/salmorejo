from kubernetes import client, watch
from k8s import Watcher

_daemonset_watcher = None
_deployment_watcher = None
_replicaset_watcher = None
_statefulset_watcher = None

def get_deployment_watcher(namespace=None):
    global _deployment_watcher
    if _deployment_watcher is None:
        _deployment_watcher = DeploymentWatcher(namespace=namespace)
    return _deployment_watcher

def get_daemonset_watcher(namespace=None):
    global _daemonset_watcher
    if _daemonset_watcher is None:
        _daemonset_watcher = DaemonsetWatcher(namespace=namespace)
    return _daemonset_watcher    

def get_replicaset_watcher(namespace=None):
    global _replicaset_watcher
    if _replicaset_watcher is None:
        _replicaset_watcher = ReplicasetWatcher(namespace=namespace)
    return _replicaset_watcher

def get_statefulset_watcher(namespace=None):
    global _statefulset_watcher
    if _statefulset_watcher is None:
        _statefulset_watcher = StatefulsetWatcher(namespace=namespace)
    return _statefulset_watcher

class DaemonsetWatcher(Watcher):
    def __init__(self, namespace=None, auto_start=False):
        self.namespace=namespace
        super().__init__(auto_start)

    def get_stream_args(self):
        if self.namespace is None:
            return [client.AppsV1Api().list_daemon_set_for_all_namespaces]
            
        return [client.AppsV1Api().list_namespaced_daemon_set,\
                self.namespace]
                
    def get_stream_kwargs(self):
        return self._get_stream_default_kwargs()

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

class ReplicasetWatcher(Watcher):
    def __init__(self, namespace=None, auto_start=False):
        self.namespace=namespace
        super().__init__(auto_start)

    def get_stream_args(self):
        if self.namespace is None:
            return [client.AppsV1Api().list_replica_set_for_all_namespaces]
            
        return [client.AppsV1Api().list_namespaced_replica_set,\
                self.namespace]
                
    def get_stream_kwargs(self):
        return self._get_stream_default_kwargs()

class StatefulsetWatcher(Watcher):
    def __init__(self, namespace=None, auto_start=False):
        self.namespace=namespace
        super().__init__(auto_start)

    def get_stream_args(self):
        if self.namespace is None:
            return [client.AppsV1Api().list_stateful_set_for_all_namespaces]
            
        return [client.AppsV1Api().list_namespaced_replica_set,\
                self.namespace]
                
    def get_stream_kwargs(self):
        return self._get_stream_default_kwargs()
