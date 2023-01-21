# Leetcode
# 76. Minimum Window Substring


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""
        # create hashmap of characters in t
        t_hashmap = {}
        for char in t:
            t_hashmap[char] = 1 + t_hashmap.get(char, 0)
        # create hashmap of characters to be added into window
        window_hashmap = {}
        # store length & indices of substring
        result_indices = [-1, -1]
        result_len = float("inf")
        # pointers for sliding window
        left = 0
        current = 0
        target = len(t_hashmap)
        # print(f"target {target}")
        # start adding chars to window
        for right in range(len(s)):
            # print(right)
            window_hashmap[s[right]] = 1 + window_hashmap.get(s[right], 0)
            # if current char in string t AND the count matches in both hashmaps, increment current
            if s[right] in t_hashmap:
                if window_hashmap[s[right]] == t_hashmap[s[right]]:
                    current += 1
            # while condition is met
            # update the result indices and length
            # increment the left pointer
            # print(window_hashmap)
            # print(f"current {current}")
            while current == target:

                # compare result lengths and store the lower value
                if (right-left+1) < result_len:
                    result_indices = [left, right]
                    result_len = right-left+1
                # remove the element at the left of the window
                window_hashmap[s[left]] -= 1
                # check if the removed element is in string t AND if the count of hashmaps is still matches
                if s[left] in t_hashmap:
                    if window_hashmap[s[left]] < t_hashmap[s[left]]:
                        current -= 1
                # increment left (to find smallest possible substring)
                left += 1
        # return the substring of indices from result_indices if result_len is not infinity
        # print(result_indices[0], result_indices[1])
        return s[result_indices[0]:result_indices[1]+1] if result_len != float("inf") else "" 
