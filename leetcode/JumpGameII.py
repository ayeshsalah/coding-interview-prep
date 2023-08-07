# Leetcode
# 45. Jump Game II

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1): # r+1 to make it inclusive
                farthest = max(farthest, i + nums[i]) # max of farthest and current index(i) and max value we can jump(nums[i]).
            jumps += 1
            l = r+1
            r = farthest
        return jumps
