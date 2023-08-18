# Leetcode
# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        j = 0
        for i in range(len(haystack)):
            result = i 
            j = 0
            while haystack[i] == needle[j]:
                if j == len(needle)-1:
                    return result
                i += 1
                j += 1

                if i == len(haystack):
                    return -1
        return -1
