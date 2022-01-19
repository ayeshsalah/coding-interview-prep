# Leetcode
# 448. Find All Numbers Disappeared in an Array
# Editted the solution for Leetcode 268

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_dict = collections.Counter(range(1, len(nums)+1))
        for num in nums:
            if nums_dict.get(num):
                nums_dict.pop(num)
                
        if nums_dict:
            return list(nums_dict.keys())
