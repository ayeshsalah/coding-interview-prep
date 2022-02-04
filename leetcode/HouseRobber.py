# Leetcode
# 198. House Robber
# https://www.youtube.com/watch?v=73r3KWiEvyk
# https://www.youtube.com/watch?v=ZwDDLAeeBM0


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1 ...]
        for n in nums:
            # choose the max of 1st and 3rd house or 2nd house. 
            # reassign the values of the houses
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2



class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]
        
        for n in range(1, len(nums)):
            dp[n+1] = max(dp[n], dp[n-1]+nums[n])
            
        return dp[len(nums)]
    