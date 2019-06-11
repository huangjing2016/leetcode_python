from typing import List


class Solution:
    def remove_element(self, nums: List[int], val:int) -> int:
        length = 0
        for index,num in enumerate(nums):
            if num != val:
                if index != length:
                    nums[length] = num
                length += 1
        return length
