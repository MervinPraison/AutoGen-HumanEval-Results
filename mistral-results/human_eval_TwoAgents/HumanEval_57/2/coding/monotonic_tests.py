# filename: monotonic_tests.py
import unittest
from my_tests import run_tests as run_custom_tests

class TestMonotonic(unittest.TestCase):
    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([4, 1, 0, -10]))

    def test_non_monotonic(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))

if __name__ == '__main__':
    unittest.main()