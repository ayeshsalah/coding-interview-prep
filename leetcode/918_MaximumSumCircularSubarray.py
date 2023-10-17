# Leetcode
# 918. Maximum Sum Circular Subarray
# https://www.youtube.com/watch?v=fxT9KjakYPM


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_min = nums[0]
        global_max = nums[0]
        current_max = 0
        current_min = 0
        total = 0
        for n in nums:
            current_max = max(n, current_max+n)
            global_max = max(global_max, current_max)
            total += n
            current_min = min(n, current_min+n)
            global_min = min(global_min, current_min)
        # check if all nums have been negative
        if global_max<0:
            return global_max
        return max(global_max, total-global_min)
        