# Leetcode
# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            # if we all the numbers in nums, we will get the unique number.
            # XOR same number returns 0. So when the same number is encountered again, it will become zero, leaving only the unique number.
            result = n ^ result
        return result