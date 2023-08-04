# Leetcode
# 189. Rotate Array
# https://www.youtube.com/watch?v=BHr381Guz3Y

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse the array
        # mod k with length of array to find new k
        # reverse the 0 to k index
        # reverse k index to end of array 
        k = k % len(nums)

        l, r = 0, len(nums)-1
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = 0, k-1
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = k, len(nums)-1
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1            
