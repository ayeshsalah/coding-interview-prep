# Leetcode
# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Since the list is sorted, compare adjacent elements and pop when they match.
        # To avoid out of bounds error, set index as 1 and compare with previous element.
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                nums.pop(index-1)
            else:
                index +=1
        return len(nums)
