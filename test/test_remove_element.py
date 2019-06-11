import unittest
from src import remove_element

class TestRemoveElement(unittest.TestCase):
    def test_return_length(self):
        solution = remove_element.Solution()
        output = solution.remove_element([3,2,2,3], 3)
        assert output == 2

    def test_modify_array(self):
        nums = [3,2,2,3]
        solution = remove_element.Solution()
        output = solution.remove_element(nums, 3)
        for i in range(2):
            assert nums[i] == 2
