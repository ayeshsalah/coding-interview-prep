# Leetcode
# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        hashmap = {}
        for i in range(len(pattern)):
            if hashmap.get(pattern[i]):
                if hashmap.get(pattern[i]) != s[i]:
                    return False
            else:
                # check if two different keys have the same value. Return False in that case. 
                if s[i] in hashmap.values():
                    return False
                hashmap[pattern[i]] = s[i]
        return True
