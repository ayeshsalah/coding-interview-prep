# Leetcode
# 134. Gas Station
# https://www.youtube.com/watch?v=lJwbPZGo05A

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if solution exists
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i]-cost[i]

            if total<0:
                total = 0
                start = i+1 # assuming next index will have positive gas.
        return start
