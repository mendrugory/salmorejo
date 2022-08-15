import unittest
from kubernetes import client
from k8s.apps.v1 import get_deployment_watcher, DeploymentWatcher
from tests import TestCaseWatcher

class DeploymentWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = DeploymentWatcher().get_stream_args()
        expected = [client.AppsV1Api().list_deployment_for_all_namespaces]
        self.check_args(actual, expected)


    def test_args_with_namespace(self):
        namespace = "test"
        actual = DeploymentWatcher(namespace).get_stream_args()
        expected = [
            client.AppsV1Api().list_namespaced_deployment,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_deployment_watcher(self):
        watcher = get_deployment_watcher()
        self.assertTrue(watcher)

if __name__ == '__main__':
    unittest.main()