import unittest

class TestCaseWatcher(unittest.TestCase):
    def check_args(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for i in range(len(actual)):
            if callable(actual[i]) and callable(expected[i]):
                self.assertEqual(actual[i].__code__.co_code, expected[i].__code__.co_code)
            else:
                self.assertEqual(actual[i], expected[i])