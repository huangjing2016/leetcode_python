import unittest
from src import count_and_say


class TestCountAndSay(unittest.TestCase):
    def test_1(self):
        solution = count_and_say.Solution()
        result = solution.count_and_say(1)
        assert result == '1'

    def test_2(self):
        solution = count_and_say.Solution()
        result = solution.count_and_say(2)
        assert result == '11'

    def test_3(self):
        solution = count_and_say.Solution()
        result = solution.count_and_say(3)
        assert result == '21'

    def test_4(self):
        solution = count_and_say.Solution()
        result = solution.count_and_say(4)
        print(result)
        assert result == '1211'

    def test_5(self):
        solution = count_and_say.Solution()
        result = solution.count_and_say(5)
        assert result == '111221'