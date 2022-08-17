from k8s.apps.v1 import get_daemonset_watcher, get_deployment_watcher, get_replicaset_watcher, get_statefulset_watcher
from k8s.core.v1 import get_configmap_watcher, get_pod_watcher, get_secret_watcher, get_service_watcher
from k8s.networking.v1 import get_ingress_watcher

KUBERNETES_CONFIGMAPS_NAMES=("configmap", "configmaps", "cm",)
KUBERNETES_DAEMONSETS_NAMES=("daemonset", "daemonsets", "ds",)
KUBERNETES_DEPLOYMENTS_NAMES=("deployments", "deployment",)
KUBERNETES_INGRESSES_NAMES=("ingress", "ingresses", "ing",)
KUBERNETES_PODS_NAMES=("pods", "pod", "po",)
KUBERNETES_REPLICASETS_NAMES=("replicaset", "replicasets", "rs",)
KUBERNETES_SECRETS_NAMES=("secret", "secrets",)
KUBERNETES_SERVICES_NAMES=("services", "service", "svc",)
KUBERNETES_STATEFULSETS_NAMES=("statefulset", "statefulsets", "sts",)

ALLOWED_K8S_OBJECTS = KUBERNETES_CONFIGMAPS_NAMES \
    + KUBERNETES_DAEMONSETS_NAMES \
    + KUBERNETES_INGRESSES_NAMES \
    + KUBERNETES_DEPLOYMENTS_NAMES\
    + KUBERNETES_PODS_NAMES \
    + KUBERNETES_REPLICASETS_NAMES \
    + KUBERNETES_SECRETS_NAMES \
    + KUBERNETES_SERVICES_NAMES \
    + KUBERNETES_STATEFULSETS_NAMES

def is_object_allowed(k8s_object):
    return k8s_object in ALLOWED_K8S_OBJECTS

def get_watcher(k8s_object):
    '''
    get_watcher(k8s_object) will return the desired watcher
    based on the k8s_object (name) given as argument.
    '''
    if k8s_object in KUBERNETES_CONFIGMAPS_NAMES:
        return get_configmap_watcher()
    if k8s_object in KUBERNETES_DAEMONSETS_NAMES:
        return get_daemonset_watcher()
    if k8s_object in KUBERNETES_DEPLOYMENTS_NAMES:
        return get_deployment_watcher()
    if k8s_object in KUBERNETES_INGRESSES_NAMES:
        return get_ingress_watcher()
    if k8s_object in KUBERNETES_PODS_NAMES:
        return get_pod_watcher()
    if k8s_object in KUBERNETES_REPLICASETS_NAMES:
        return get_replicaset_watcher()
    if k8s_object in KUBERNETES_SECRETS_NAMES:
        return get_secret_watcher()
    if k8s_object in KUBERNETES_SERVICES_NAMES:
        return get_service_watcher()
    if k8s_object in KUBERNETES_STATEFULSETS_NAMES:
        return get_statefulset_watcher()        
