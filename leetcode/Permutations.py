# Leetcode
# 46. Permutations
# https://www.youtube.com/watch?v=s7AvT7cGdSo

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            permutations = self.permute(nums)
            for perms in permutations:
                perms.append(n)
            result.extend(permutations)
            nums.append(n)
        return result
