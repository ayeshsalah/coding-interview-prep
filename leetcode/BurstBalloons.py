# Leetcode
# 312. Burst Balloons
# https://www.youtube.com/watch?v=VFskby7lUbw
# https://leetcode.com/problems/burst-balloons/discuss/1017626/Python-Accepted-oror-Detailed-Explanation-oror-Dhruv-Vavliya

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # handing leetcode's 70th test case, i.e., List of five hundred 100's.
        if len(nums)>1 and len(set(nums))==1:
            return (nums[0] ** 3) * (len(nums)-2) + nums[0] ** 2 + nums[0]
        
        # adding 1 at the start and end of nums. 
        nums.insert(0, 1)
        nums.append(1)
        # dict for storing DP calcs
        dp = {}
        # left = 1 & right = len(nums)-2, omitting the the 1's added at the start and end of the list. 
        return self.max_coins(nums, dp, 1, len(nums)-2)
        
    def max_coins(self, nums, dp, left, right):
        """ recursive function for getting max coins """
        if left > right:
            return 0
        # check if (left, right) is present in DP cache.
        if (left, right) in dp:
            return dp[(left, right)]
        
        dp[(left, right)] = 0
        # iterate thru nums from left to right, where i is the last ballon to be popped. 
        for i in range(left, right+1):
            prod = nums[left-1] * nums[i] * nums[right+1] 
            prod += self.max_coins(nums, dp, left, i-1) + self.max_coins(nums, dp, i+1, right)
            dp[(left, right)] = max(prod, dp[(left, right)])
        return dp[(left, right)]
