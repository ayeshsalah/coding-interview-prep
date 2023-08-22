# Leetcode
# 209. Minimum Size Subarray Sum
# https://www.youtube.com/watch?v=aYqYMIqZx5s

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_size = min(min_size, right-left+1)
                total -= nums[left]
                left += 1   
        return min_size if min_size != float("inf") else 0
