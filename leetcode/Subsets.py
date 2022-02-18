# Leetcode
# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in nums:
            result += [item+[i] for item in result]                
        return result
