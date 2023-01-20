# Leetcode
# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = {} # create hashmap of s1 values and frequencies
        for c in s1:
            s1_counter[c] = 1 + s1_counter.get(c, 0)

        window_size = len(s1) # window size 
        # slide the window and compare hashmaps
        for i in range(len(s2)-window_size+1):
            s2_counter = {}
            for c in s2[i:i+window_size]:
                s2_counter[c] = 1 + s2_counter.get(c, 0)
            if s2_counter == s1_counter:
                return True
        return False
