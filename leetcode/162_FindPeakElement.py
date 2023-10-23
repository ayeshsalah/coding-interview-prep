# Leetcode 
# 162. Find Peak Element
# https://www.youtube.com/watch?v=kMzJy9es7Hc


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            # check if left neighbour is greater
            if mid > 0 and nums[mid-1] > nums[mid]:
                right = mid -1
            # check if right neighbour is greater
            elif mid < len(nums)-1 and nums[mid+1] > nums[mid]:
                left = mid + 1
            else:
                return mid            
