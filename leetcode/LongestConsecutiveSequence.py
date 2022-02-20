# Leetcode
# 128. Longest Consecutive Sequence
# https://www.youtube.com/watch?v=P6RZZMu_maU


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
         
        for i in nums:
            # start of the seqeunce is detected by checking for a previous neighbour in the num_set
            # if num is not the start of a sequence; 
            # run a while loop until the next neighbours are in the numset
            # store the max of the current result and length
            if (i-1) not in num_set:
                length = 0
                while (i+length) in num_set:
                    length += 1
                result = max(result, length)
        return result
