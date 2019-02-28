# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False

        len = 1
        while x//(10**len):
            len += 1

        while x and len > 0:
            if len == 1:
                return True

            left = x // 10**(len-1)
            right = x % 10
            if left != right:
                return False

            x = x % 10 **(len-1)
            x = x // 10

            len -= 2

        return True

if __name__ == '__main__':
    s = Solution()
    result = s.isPalindrome(213212)
    print(result)