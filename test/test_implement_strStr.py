import unittest
from src import implement_strStr


class TestImplementstrStr(unittest.TestCase):
    def test_return_index(self):
        haystack = 'hello'
        needle = 'll'
        solution = implement_strStr.Solution()
        output = solution.strStr(haystack, needle)
        assert output == 2

    def test_not_find(self):
        haystack = 'hello'
        needle = 'lle'
        solution = implement_strStr.Solution()
        output = solution.strStr(haystack, needle)
        assert output == -1

    def test_needle_is_empty(self):
        haystack = 'hello'
        needle = ''
        solution = implement_strStr.Solution()
        output = solution.strStr(haystack, needle)
        assert output == 0

    def test_needle_gt_haystack(self):
        haystack = 'aaa'
        needle = 'aaaa'
        solution = implement_strStr.Solution()
        output = solution.strStr(haystack, needle)
        assert output == -1
