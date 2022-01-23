# Leetcode
# 746. Min Cost Climbing Stairs
# Similar to leetcode 70
# https://www.youtube.com/watch?v=ktmzAZWkEZ0


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # watch video for detailed explanation of DP
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
