# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2:
            return False

        par_dict = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        l = []
        for i in range(len(s)):
            if len(l) != 0 and par_dict.get(s[i]) == l[-1]:
                l.pop()
            else:
                l.append(s[i])
        return 0 == len(l)


if __name__ == '__main__':
    solution = Solution()
    res = solution.isValid('{[]}')
    print(res)