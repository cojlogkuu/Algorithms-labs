import unittest
from src.min_distance_of_chess_horse import get_min_distance_of_chess_horse

class Test(unittest.TestCase):
    def test_given_input(self):
        get_min_distance_of_chess_horse('../resources/input', '../resources/output')
        with open('../resources/output', 'r') as file:
            result = int(file.readline())
        self.assertEqual(result, 6)

    def test_wrong_input(self):
        get_min_distance_of_chess_horse('../resources/wrong_input', '../resources/wrong_output')
        with open('../resources/wrong_output', 'r') as file:
            result = int(file.readline())
        self.assertEqual(result, -1)