# Leetcode
# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            elif num == 2:
                c2 += 1
            
        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2
