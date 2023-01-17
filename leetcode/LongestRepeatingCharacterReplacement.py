# Leetcode
# 424. Longest Repeating Character Replacement
# https://www.youtube.com/watch?v=gqXU1UyA8pk
# https://leetcode.com/problems/longest-repeating-character-replacement/solutions/765776/python-two-pointers-process-for-coding-interviews/


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

#### Additional Solution ####


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        hashmap = {}
        for right in range(0, len(s)):
            if s[right] in hashmap.keys():
                hashmap[s[right]] += 1
            else:
                hashmap[s[right]] = 1
            max_freq = max(hashmap.values())
            if (right-left+1) - max_freq <= k:
                max_len = max(max_len, (right-left+1))
            else:
                hashmap[s[left]] -= 1
                left += 1
        return max_len
