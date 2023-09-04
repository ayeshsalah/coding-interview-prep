# Leetcode
# 228. Summary Ranges


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            # i+1 is in bounds. Check if current number+1 is equal to the next element.
            while i+1 < len(nums) and nums[i]+1 == nums[i+1]:
                i += 1
            # if start and current number are the same, append single number
            # else append the start and end.
            if nums[i] == start:
                result.append(str(start))
            else:
                result.append(str(start)+"->"+str(nums[i]))
            i += 1
        return result
