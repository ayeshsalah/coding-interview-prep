# Leetcode
# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
# Similar to leetcode 33


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid] >= nums[right]:
                # we search the right sorted array
                # minimize the array by making mid+1 the left
                left = mid+1
            elif nums[mid] <= nums[right]:
                # we search the left sorted array
                # minimize the array by making mid the right
                right = mid
        return nums[left]
