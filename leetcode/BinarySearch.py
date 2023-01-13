# Leetcode
# 704. Binary Search


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            # (l + r) // 2 can lead to overflow
            # Find the distance between the 2 pointers, divide it by 2 and add the left index to the result, to find the mid point.
            middle = left + ((right-left)//2) 
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1
