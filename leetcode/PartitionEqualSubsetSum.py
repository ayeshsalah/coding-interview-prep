# Leetcode
# 416. Partition Equal Subset Sum
# https://www.youtube.com/watch?v=IsvocB5BJhw


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2:
            return False
        
        dp = set()
        dp.add(0)
        
        target = nums_sum // 2 
        for i in range(len(nums)):
            temp = set()
            for item in dp:
                temp_sum = item+nums[i]
                if temp_sum == target:
                    return True
                temp.add(temp_sum)
            dp.update(temp)
        
        if target in dp:
            return True
        return False
