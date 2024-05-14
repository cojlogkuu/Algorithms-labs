import unittest
from src.max_length_of_electric_wire import find_max_length_of_wive


class Test(unittest.TestCase):

    def test_same_heights(self):
        self.assertEqual(find_max_length_of_wive(2, [3, 3, 3]), 5.66)

    def test_all_heights_1(self):
        self.assertEqual(find_max_length_of_wive(100, [1, 1, 1, 1]), 300)

    def test_5_heights(self):
        self.assertEqual(find_max_length_of_wive(4, [100, 2, 100, 2, 100]), 396.32)

    def test_many_heights(self):
        heights = [56, 18, 17, 94, 23, 7, 21, 94, 29, 54, 44, 26, 86, 79, 4, 15, 5, 91, 25, 17, 88, 66, 28, 1, 95, 97,
                   60, 93, 40, 70, 75, 48, 38, 51, 34, 52, 87, 8, 62, 77, 35, 52, 3, 93, 34, 57, 51, 11, 39, 72]
        self.assertEqual(find_max_length_of_wive(4, heights), 2738.18)


if __name__ == '__main__':
    unittest.main()
