# filename: test_sorting.py
import unittest
from sorting_module import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(sort_array([]))
        self.assertTrue(sorted([]) == [])

    def test_single_element(self):
        array = [1]
        self.assertListEqual(array, sort_array(array))

    def test_sum_even(self):
        array = [3, 4, 5]
        expected = [5, 4, 3]
        self.assertListEqual(expected, sort_array(array))

    def test_sum_odd(self):
        array = [1, 2, 3]
        expected = [3, 2, 1]
        self.assertListEqual(expected, sort_array(array))

if __name__ == "__main__":
    unittest.main()