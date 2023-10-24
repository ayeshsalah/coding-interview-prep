# Leetcode
# 34. Find First and Last Position of Element in Sorted Array
# https://www.youtube.com/watch?v=4sQL7R5ySUU

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]
        

    def binary_search(self, nums, target, search_left):
        left = 0
        right = len(nums)-1
        result = -1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] > target:
                right = middle-1
            elif nums[middle] < target:
                left = middle + 1
            else:
                result = middle
                if search_left:
                    right = middle-1
                else:
                    left = middle+1
        return result
    