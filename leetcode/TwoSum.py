# Leetcode
# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for index, num in enumerate(nums):
            diff = target-num
            if diff in visited.keys():
                return [visited[diff], index]
            visited[num] = index
        