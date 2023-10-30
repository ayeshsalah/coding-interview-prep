# Leetcode
# 137. Single Number II
# https://www.youtube.com/watch?v=MInz2ao4wao


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0 
        for n in nums:
            ones = (n ^ ones) & ~twos
            twos = (n ^ twos) & ~ones
        return ones
