# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    MAX_NUM = 2 ** 31
    def reverse(self, x: int) -> int:
        res = 0
        flag = 1 if x >=0 else -1

        while x != 0:
            res = abs(x) % 10 + res * 10 # 此处必须取绝对值,python 取余算法负数是向下取整
            x = abs(x) // 10

        return res * flag if res < self.MAX_NUM else 0

if __name__ == '__main__':
    x = -123
    solution = Solution()
    print(solution.reverse(x))


