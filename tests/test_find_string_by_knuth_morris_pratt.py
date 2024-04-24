import unittest
from src.find_string_by_knuth_morris_pratt import find_string_by_knuth_morris_pratt


class Test(unittest.TestCase):

    def test_normal_text(self):
        needle = 'Dodko'
        haystack = 'My name is Dodko. Dodko qwe ewq!!!'
        self.assertEqual(find_string_by_knuth_morris_pratt(haystack, needle), [11, 18])

    def test_repeated_words(self):
        needle = 'aabbaaab'
        haystack = 'cccaabbaaabaaaaabbaaabbbbbaabbaaab'
        self.assertEqual(find_string_by_knuth_morris_pratt(haystack, needle), [3, 14, 26])

    def test_no_matches(self):
        needle = 'qwerty'
        haystack = 'kvjknsodnsjfsjpfjngpjasnjgadjpfsgjnoda'
        self.assertEqual(find_string_by_knuth_morris_pratt(haystack, needle), [])

    def test_gaps(self):
        needle = ' '
        haystack = 'Bodya lets go play football. '
        self.assertEqual(find_string_by_knuth_morris_pratt(haystack, needle), [5, 10, 13, 18, 28])
