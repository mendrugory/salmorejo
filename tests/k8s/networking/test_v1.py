import unittest
from kubernetes import client
from k8s.networking.v1 import get_ingress_watcher, IngressWatcher
from tests import TestCaseWatcher

class IngressWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = IngressWatcher().get_stream_args()
        expected = [client.NetworkingV1Api().list_ingress_for_all_namespaces]
        self.check_args(actual, expected)

    def test_args_with_namespace(self):
        namespace = "test"
        actual = IngressWatcher(namespace).get_stream_args()
        expected = [
            client.NetworkingV1Api().list_namespaced_ingress,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_ingress_watcher(self):
        watcher = get_ingress_watcher()
        self.assertTrue(watcher)


if __name__ == '__main__':
    unittest.main()