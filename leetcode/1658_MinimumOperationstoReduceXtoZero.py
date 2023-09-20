# Leetcode
# 1658. Minimum Operations to Reduce X to Zero 
# https://www.youtube.com/watch?v=xumn16n7njs


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        left = 0 
        current_sum = 0
        max_window = -1
        for right in range(len(nums)):
            current_sum += nums[right]
            # If the sum of this sliding window (subarray) exceeds the target, keep reducing the window size (by increasing left) until its sum becomes <= target.
            while left<=right and current_sum > target:
                current_sum -= nums[left]
                left += 1
            # If the sum becomes equal to the target, compare the length, and store if it exceeds the previous length.
            if current_sum == target:
                max_window = max(max_window, right-left+1)

        return -1 if max_window==-1 else len(nums)-max_window
