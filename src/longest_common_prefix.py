# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return res

        min = sorted(strs)[0]

        for i in range(len(min)):
            for s in strs:
                if s[i] != min[i]:
                    return res
            res += min[i]

        return res

if __name__ == '__main__':
    a = ['abc','ab']
    soulution = Solution()
    res = soulution.longestCommonPrefix(a)
    print(res)

