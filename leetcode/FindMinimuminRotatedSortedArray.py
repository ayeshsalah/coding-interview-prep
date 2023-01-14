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
            # if middle is greater than right, search right sorted array
            if nums[mid] > nums[right]:
                # minimize the array by making mid+1 the left
                left = mid+1
            # if middle is less than right, search left sorted array 
            elif nums[mid] < nums[right]:
                # minimize the array by making mid the right
                right = mid
        return nums[left]
