# filename: my_tests.py
import unittest
from sorting import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(sort_array([]))
        self.assertTrue(sorted([]) == [])

    def test_single_element(self):
        a = [5]
        sorted_a = sort_array(a)
        self.assertEqual(sorted_a, a)

    def test_even_sum(self):
        a = [2, 4, 3, 0, 1, 5]
        sorted_a = sort_array(a)
        self.assertFalse(sorted_a == a)
        self.assertTrue(sorted_a[:] == [0, 1, 2, 3, 4, 5])

    def test_odd_sum(self):
        a = [2, 4, 3, 0, 1, 5, 6]
        sorted_a = sort_array(a)
        self.assertFalse(sorted_a == a)
        self.assertTrue(sorted_a[:] == [6, 5, 4, 3, 2, 1, 0])

if __name__ == "__main__":
    unittest.main()