# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []

        # for x in range(len(nums)-1):
        #     for y in range(x+1, len(nums)):
        #         if nums[x] + nums[y] == target:
        #             return [x, y]
        # return []

        buf_dict = {}
        for i in range(len(nums)):
            if nums[i] in buf_dict: # 如果满足相加为target条件的值存在
                return [buf_dict[nums[i]], i]
            else:
                buf_dict[target - nums[i]] = i # 保存下之前数值所在的位置，key为相加为target的所需值

        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 26
    s = Solution()
    result = s.twoSum(nums, target)
    print(result)