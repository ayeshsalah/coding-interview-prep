# Leetcode
# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        
        return s_counter == t_counter
        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        return s_dict == t_dict
