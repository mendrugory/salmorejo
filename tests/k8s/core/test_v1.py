import unittest
from kubernetes import client
from k8s.core.v1 import get_pod_watcher, get_service_watcher, PodWatcher, ServiceWatcher
from tests import TestCaseWatcher

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