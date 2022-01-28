# Leetcode
# 424. Longest Repeating Character Replacement
# https://www.youtube.com/watch?v=gqXU1UyA8pk

#TODO add explanation comments 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        result = 0
        maxfreq = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxfreq = max(maxfreq, count[s[right]])        
            # while (right-left+1) - max(count.values()) > k:
            while (right-left+1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right-left+1)
        return result
