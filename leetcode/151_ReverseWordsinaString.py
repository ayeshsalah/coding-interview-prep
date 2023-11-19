# Leetcode 
# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


########################

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for w in s.split()[::-1]:
            result.append(w)
        return " ".join(result)
