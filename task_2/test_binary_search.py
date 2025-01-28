import unittest
from binary_search import binary_search_with_upper_bound

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.sorted_arr = [1.2, 2.5, 3.8, 4.4, 5.9, 7.1]

    def test_exact_match(self):
        self.assertEqual(binary_search_with_upper_bound(self.sorted_arr, 3.8), (1, 3.8))

    def test_upper_bound_exists(self):
        self.assertEqual(binary_search_with_upper_bound(self.sorted_arr, 6.0), (3, 7.1))

    def test_upper_bound_start(self):
        self.assertEqual(binary_search_with_upper_bound(self.sorted_arr, 0.5), (2, 1.2))

    def test_upper_bound_end(self):
        self.assertEqual(binary_search_with_upper_bound(self.sorted_arr, 8.0), (3, None))

    def test_empty_array(self):
        self.assertEqual(binary_search_with_upper_bound([], 5), (0, None))

    def test_all_elements_smaller(self):
        self.assertEqual(binary_search_with_upper_bound(self.sorted_arr, 10.0), (3, None))

if __name__ == "__main__":
    unittest.main()