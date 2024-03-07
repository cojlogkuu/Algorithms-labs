import unittest
from src.find_range_of_unsorted_array import find_not_sort_range


class Test(unittest.TestCase):

    def test_simple_array(self):
        array1 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        array2 = [1, 3, 6, 8, 4, 11, 5, 10, 12, 16]
        array3 = [1, 2, 3, 88, 66, 44, 66, 99, 55, 101, 102, 103, 104, 106, 106]
        self.assertEqual(find_not_sort_range(array1), (3, 9))
        self.assertEqual(find_not_sort_range(array2), (2, 7))
        self.assertEqual(find_not_sort_range(array3), (3, 8))

    def test_sorted_array(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(find_not_sort_range(array), (-1, -1))

    def test_full_not_sorted_array(self):
        array = [32, 16, 12, 4, 5, 0, -6, -9, -10]
        self.assertEqual(find_not_sort_range(array), (0, 8))

    def test_one_element_array(self):
        array = [322]
        self.assertEqual(find_not_sort_range(array), (-1, -1))


if __name__ == '__main__':
    unittest.main()
