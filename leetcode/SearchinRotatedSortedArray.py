# Leetcode
# 33. Search in Rotated Sorted Array
# https://www.youtube.com/watch?v=U8XENwh8Oy8

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
      
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # we are in left sorted array
                # if target is greater then middle then search the right sorted array
                if target > nums[mid]:
                    left = mid+1
                # if target is less than middle and less than the left most element in left sorted array, search the right sorted array
                elif target < nums[mid] and target < nums[left]:
                    left = mid+1
                # if target is less then mid but greater than left, continue searching the left sorted array
                else:
                    right = mid-1
            else:
                # we are in right sorted array
                # if target is lesser then middle then search the left sorted array
                if target < nums[mid]:
                    right = mid-1
                # if target is greater than middle and greater than the right most element in right sorted array, search the left sorted array
                elif target > nums[mid] and target > nums[right]:
                    right = mid-1
                # if target is greater then mid but lesser than right, continue searching the right sorted array 
                else:
                    left = mid+1
        return -1
