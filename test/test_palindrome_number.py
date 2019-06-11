import unittest
from src import palindrome_number


class TestPalindromeNumber(unittest.TestCase):
    def test_negative_is_false(self):
        solution = palindrome_number.Solution()
        result = solution.isPalindrome(-20)
        assert result is False

    def test_121_is_true(self):
        solution = palindrome_number.Solution()
        result = solution.isPalindrome(121)
        assert result is True

    def test_12_is_false(self):
        solution = palindrome_number.Solution()
        result = solution.isPalindrome(12)
        assert result is False
