import unittest
from src.min_number_of_beers import get_min_number_of_beers


class Test(unittest.TestCase):
    def test_two_beers(self):
        self.assertEqual(get_min_number_of_beers(2, 2, 'NY YN'), 2)

    def test_four_beers(self):
        self.assertEqual(get_min_number_of_beers(7, 4, 'YNNY YYNN NYYN NNYY YNYY YYNN NYNY'), 2)
        self.assertEqual(get_min_number_of_beers(7, 4, 'YNNY YYNN NNYN NNYY YNYY YYNN NYNY'), 3)

    def test_three_beers(self):
        self.assertEqual(get_min_number_of_beers(6, 3, 'YNN YNY YNY NYY NYY NYN'), 2)
        self.assertEqual(get_min_number_of_beers(6, 3, 'YYN YYY YYY YYY YNY YYY'), 1)

    def test_one_beer(self):
        self.assertEqual(get_min_number_of_beers(2, 1, 'Y Y'), 1)


if __name__ == '__main__':
    unittest.main()
