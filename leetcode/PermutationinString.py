# Leetcode
# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = collections.Counter(s1) # create hashmap of s1 values and frequencies
        window_size = len(s1) # window size 
        # slide the window and compare hashmaps
        for i in range(len(s2)-window_size+1):
            if collections.Counter(s2[i:i+window_size]) == s1_counter:
                return True
        return False
