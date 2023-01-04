#LeetCode 
#3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start_idx = 0
        substr = {}
        for index, letter in enumerate(s):
            if letter in substr.keys() and start_idx<=substr[letter]:
                # if letter in hashmap move the start index to the index after the duplicate element's index. 
                start_idx = substr[letter]+1
            else:
                # if new letter is found, compare existing max length and current substring's len and store larger value.
                max_len = max(max_len, index-start_idx+1) # +1 as index starts from 0 in python
            substr[letter] = index # add letter to the hashmap
        return max_len

