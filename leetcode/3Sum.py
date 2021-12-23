# Leetcode
# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target_sum = 0 
        sorted_nums = sorted(nums)
        result = set() # Set is used to ensure duplicate triplets are not added.
        for i in range(len(sorted_nums)-1): # -1 as last element will be right pointer.
            first = i
            left = i+1
            right = len(sorted_nums)-1
            while left<right:
                current_sum = sorted_nums[first]+sorted_nums[left]+sorted_nums[right]
                # if current sum is the target sum, add a tuple of triplets to result set. 
                if current_sum == target_sum:
                    # add tuple of triplets 
                    result.add((sorted_nums[first], sorted_nums[left], sorted_nums[right]))
                    left +=1
                    right -=1
                # current sum is less than target sum, move the left pointer.
                elif current_sum < target_sum:
                    left += 1
                # current sum is more than target sum, move the right pointer.
                elif current_sum > target_sum:
                    right -=1
        # convert set of tuples to list of lists 
        return list(result)
