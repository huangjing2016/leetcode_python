import unittest
from src import roman_to_integer


class TestRomanToInteger(unittest.TestCase):
    def test_same_char(self):
        solution = roman_to_integer.Solution()
        output = solution.romanToInt('III')
        assert output == 3

    def test_left_lt_right(self):
        solution = roman_to_integer.Solution()
        output = solution.romanToInt('IV')
        assert output == 4

    def test_left_gt_right(self):
        solution = roman_to_integer.Solution()
        output = solution.romanToInt('LVIII')
        assert output == 58

    def test_mix_char(self):
        solution = roman_to_integer.Solution()
        output = solution.romanToInt('MCMXCIV')
        assert output == 1994
