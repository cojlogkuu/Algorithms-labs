import unittest
from src.min_length_of_cable_for_communication_wells import get_min_length_of_cable


class Test(unittest.TestCase):

    def test_simple_graph(self):
        self.assertEqual(get_min_length_of_cable('../resources/communication_wells_1.csv'), 19)
        self.assertEqual(get_min_length_of_cable('../resources/communication_wells_2.csv'), 37)

    def test_not_connected_wells(self):
        self.assertEqual(get_min_length_of_cable('../resources/communication_wells_not_connected.csv'), -1)


if __name__ == '__main__':
    unittest.main()
