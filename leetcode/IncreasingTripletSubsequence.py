# Leetcode
# 334. Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = smaller = float("inf")
        
        for index in range(len(nums)):
            if nums[index] <= smallest:
                smallest = nums[index]
            elif nums[index] <= smaller:
                smaller = nums[index]
            else:
                return True
        return False
