# LeetCode
# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # TC : O(N)
        # SC : O(1)
        max_sum = nums[0]
        current_sum = 0
        for n in nums:
            # if negative prefix is found, reset current sum to 0. 
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_sum = max(max_sum, current_sum)
        return max_sum
