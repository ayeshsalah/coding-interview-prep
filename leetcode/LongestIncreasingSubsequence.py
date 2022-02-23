# Leetcode
# 300. Longest Increasing Subsequence
# https://www.youtube.com/watch?v=cjWnW0hdF1Y


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Default LIS at all positions is 1
        result = [1] * len(nums)
        
        # Bottom Up DP approach; O(n^2)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                # check the num to the left is smaller than the num to the right
                # if true then assign the max of the current value and (1 + the element on the left)
                if nums[i] < nums[j]:
                    result[i] = max(result[i], 1+result[j])
                # else the result[i] will not be updated
        # print(result)
        return max(result)
