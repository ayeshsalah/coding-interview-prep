# Leetcode
# 152. Maximum Product Subarray
# https://www.youtube.com/watch?v=lXVy6YWFcRM


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) 
        curr_min = 1
        curr_max = 1
        
        for n in nums:
            # handle 0; use 1 instead to in effect ignore the 0
            if n == 0:
                curr_min = 1
                curr_max = 1
                continue
            # if all positive nums, the product keep increasing
            # if consecutive negative, the product could increase
            # To account for that, we keep track of max and min and find th emax from them            
            temp_max = n*curr_max
            temp_min = n*curr_min
            curr_max = max(temp_max, temp_min, n)
            curr_min = min(temp_max, temp_min, n)
            res = max(res, curr_max, curr_min)
        return res
