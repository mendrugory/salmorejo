import unittest
from kubernetes import client
from k8s.apps.v1 import get_daemonset_watcher, get_deployment_watcher,\
    get_replicaset_watcher, get_statefulset_watcher,\
    DaemonsetWatcher, DeploymentWatcher, ReplicasetWatcher, StatefulsetWatcher
from tests import TestCaseWatcher


class DaemonsetWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = DaemonsetWatcher().get_stream_args()
        expected = [client.AppsV1Api().list_daemon_set_for_all_namespaces]
        self.check_args(actual, expected)


    def test_args_with_namespace(self):
        namespace = "test"
        actual = DeploymentWatcher(namespace).get_stream_args()
        expected = [
            client.AppsV1Api().list_namespaced_daemon_set,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_daemonset_watcher(self):
        watcher = get_daemonset_watcher()
        self.assertTrue(watcher)


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


class ReplicasetWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = ReplicasetWatcher().get_stream_args()
        expected = [client.AppsV1Api().list_replica_set_for_all_namespaces]
        self.check_args(actual, expected)


    def test_args_with_namespace(self):
        namespace = "test"
        actual = ReplicasetWatcher(namespace).get_stream_args()
        expected = [
            client.AppsV1Api().list_namespaced_replica_set,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_replicaset_watcher(self):
        watcher = get_replicaset_watcher()
        self.assertTrue(watcher)


class StatefulsetWatcherTest(TestCaseWatcher):
    def test_args_without_namespace(self):
        actual = StatefulsetWatcher().get_stream_args()
        expected = [client.AppsV1Api().list_stateful_set_for_all_namespaces]
        self.check_args(actual, expected)


    def test_args_with_namespace(self):
        namespace = "test"
        actual = StatefulsetWatcher(namespace).get_stream_args()
        expected = [
            client.AppsV1Api().list_namespaced_stateful_set,
            namespace
        ]
        self.check_args(actual, expected)

    def test_get_statefulset_watcher(self):
        watcher = get_statefulset_watcher()
        self.assertTrue(watcher)


if __name__ == '__main__':
    unittest.main()