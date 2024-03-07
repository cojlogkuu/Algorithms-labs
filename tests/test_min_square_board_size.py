import unittest
from src.min_square_board_size import get_min_square_size


class Test(unittest.TestCase):
    def test_example_values(self):
        self.assertEqual(get_min_square_size(10, 2, 3), 9)
        self.assertEqual(get_min_square_size(2, 1000000000, 999999999), 1999999998)
        self.assertEqual(get_min_square_size(4, 1, 1), 2)

    def test_additional_values(self):
        self.assertEqual(get_min_square_size(11, 4, 2), 12)
        self.assertEqual(get_min_square_size(11, 2, 4), 12)
        self.assertEqual(get_min_square_size(10, 100, 11), 110)

    def test_number_equal_zero(self):
        self.assertEqual(get_min_square_size(0, 3, 22), 0)


if __name__ == '__main__':
    unittest.main()

