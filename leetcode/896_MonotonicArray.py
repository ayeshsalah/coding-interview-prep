# Leetcode
# 896. Monotonic Array


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_flag_set = False
        flag = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                if is_flag_set and flag == -1:
                    return False
                else:
                    is_flag_set =True
                    flag = 1
            elif nums[i] > nums[i+1]:
                if is_flag_set and flag == 1:
                    return False
                else:
                    is_flag_set =True
                    flag = -1
        return True
