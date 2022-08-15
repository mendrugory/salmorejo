from k8s.apps.v1 import get_deployment_watcher
from k8s.core.v1 import get_pod_watcher, get_service_watcher

KUBERNETES_DEPLOYMENTS_NAMES=("deployments", "deployment",)
KUBERNETES_PODS_NAMES=("pods", "pod", "po",)
KUBERNETES_SERVICES_NAMES=("services", "service", "svc",)
ALLOWED_K8S_OBJECTS = KUBERNETES_PODS_NAMES + KUBERNETES_DEPLOYMENTS_NAMES + KUBERNETES_SERVICES_NAMES

def is_object_allowed(k8s_object):
    return k8s_object in ALLOWED_K8S_OBJECTS

def get_watcher(k8s_object):
    '''
    get_watcher(k8s_object) will return the desired watcher based on the k8s_object (name) given as argument.
    '''
    if k8s_object in KUBERNETES_DEPLOYMENTS_NAMES:
        return get_deployment_watcher()
    if k8s_object in KUBERNETES_PODS_NAMES:
        return get_pod_watcher()
    if k8s_object in KUBERNETES_SERVICES_NAMES:
        return get_service_watcher()
