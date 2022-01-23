# Leetcode
# 70. Climbing Stairs
# https://www.youtube.com/watch?v=Y0lT9Fck7qI


class Solution:
    def climbStairs(self, n: int) -> int:
        # watch video for detailed analysis on DP 
        two = 1
        one = 1
        
        for i in range(n-1):           
            temp = one + two
            two = one
            one = temp
        return one
