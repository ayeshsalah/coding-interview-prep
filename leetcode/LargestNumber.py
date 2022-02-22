# Leetcode
# 179. Largest Number
# https://www.youtube.com/watch?v=WDx6Y4i4xJ8


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # convert nums to str
        for i, n in enumerate(nums):
            nums[i] = str(n)
        
        def compare(n1, n2):
            # comparing the added strings in both combinations. 
            if n1+n2 > n2+n1:
                return -1 # when we want to return n1 first; if n1 has larger significant digit.
            else:
                return 1 # when we want to return n2 first. OR if there is a tie.
        
        from functools import cmp_to_key
        # sorted nums based on key
        nums = sorted(nums, key = cmp_to_key(compare))
        
        # str->int->str to handle leading zeros
        return str(int("".join(nums)))
