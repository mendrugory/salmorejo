import unittest
from kubernetes import client
from k8s.core.v1 import get_configmap_watcher, get_pod_watcher,\
    get_service_watcher, get_secret_watcher,\
    ConfigmapWatcher, PodWatcher, SecretWatcher, ServiceWatcher
from tests import TestCaseWatcher


class ConfigmapWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = ConfigmapWatcher().get_stream_args()
        expected = [client.CoreV1Api().list_config_map_for_all_namespaces]
        self.check_args(actual, expected)


    def test_args_with_namespace(self):
        namespace = "test"
        actual = ConfigmapWatcher(namespace).get_stream_args()
        expected = [
            client.CoreV1Api().list_namespaced_config_map,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_configmap_watcher(self):
        watcher = get_configmap_watcher()
        self.assertTrue(watcher)


class PodWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = PodWatcher().get_stream_args()
        expected = [client.CoreV1Api().list_pod_for_all_namespaces]
        self.check_args(actual, expected)


    def test_args_with_namespace(self):
        namespace = "test"
        actual = PodWatcher(namespace).get_stream_args()
        expected = [
            client.CoreV1Api().list_namespaced_pod,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_pod_watcher(self):
        watcher = get_pod_watcher()
        self.assertTrue(watcher)


class SecretWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = SecretWatcher().get_stream_args()
        expected = [client.CoreV1Api().list_secret_for_all_namespaces]
        self.check_args(actual, expected)


    def test_args_with_namespace(self):
        namespace = "test"
        actual = SecretWatcher(namespace).get_stream_args()
        expected = [
            client.CoreV1Api().list_namespaced_secret,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_secret_watcher(self):
        watcher = get_secret_watcher()
        self.assertTrue(watcher)        


class ServiceWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = ServiceWatcher().get_stream_args()
        expected = [client.CoreV1Api().list_service_for_all_namespaces]
        self.check_args(actual, expected)


    def test_args_with_namespace(self):
        namespace = "test"
        actual = ServiceWatcher(namespace).get_stream_args()
        expected = [
            client.CoreV1Api().list_namespaced_service,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_service_watcher(self):
        watcher = get_service_watcher()
        self.assertTrue(watcher)


if __name__ == '__main__':
    unittest.main()