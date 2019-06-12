# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if not needle:
        #     return 0
        #
        # for index, s in enumerate(haystack):
        #     if s == needle[0]:
        #         if len(haystack) - index < len(needle):
        #             return -1
        #         flag = 1
        #         for index_n, n in enumerate(needle):
        #             if n != haystack[index+index_n]:
        #                 flag = 0
        #                 break
        #         if flag == 1:
        #             return index
        #
        # return -1

        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
