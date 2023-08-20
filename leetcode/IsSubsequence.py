# Leetcode
# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        subseq = 0
        for i in range(len(t)):
            if subseq < len(s) and s[subseq] == t[i]:
                subseq += 1
        return subseq == len(s)
