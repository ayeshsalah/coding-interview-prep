# Leetcode
# 213. House Robber II
# https://www.youtube.com/watch?v=rWAJCfYYOvM

class Solution:
    # Check Leetcode #198
    def rob(self, nums: List[int]) -> int:
        # handling edge case; 1 item list
        if len(nums) == 1:
            return nums[0]
        # return max of list with first element excluded and list with last element excluded. 
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
    
    def rob_helper(self, nums):
        dp = [0] * (len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        for n in range(1, len(nums)):
            # select max of current element or sum of prev and next elements
            dp[n+1] = max(dp[n], dp[n-1]+nums[n])
        return dp[len(nums)]
