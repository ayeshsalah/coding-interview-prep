#LeetCode 
#3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len_counter = 0
        start_idx = 0
        substr = {}
        for curr_idx, item in enumerate(s):
            if item in substr.keys() and start_idx<=substr[item]: 
                start_idx = substr[item] + 1
            else:
                max_len_counter = max(max_len_counter, curr_idx - start_idx+1) #find max length every iteration 
            substr[item] = curr_idx         #add/update hashtable
        return  max_len_counter
