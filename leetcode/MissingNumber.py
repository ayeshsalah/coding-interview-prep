# Leetcode
# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # hashmap solution
        nums_dict = collections.Counter(range(len(nums)+1))
        for num in nums:
            if nums_dict.get(num):
                nums_dict.pop(num)
                
        if nums_dict:
            return list(nums_dict.keys())[0]

        ###########################################
        # math solution
        return sum(range(len(nums)+1)) - sum(nums)

        ###########################################
        # bit manipulation solution
        # When the XOR operator ^ is used (result ^= i & result ^= num), 2 same integers would get the result of 0 (x^x = 0). 
        # Finally, the result would only contain the number that couldn't find its pair, which is the missing number.
        result = 0 
        for i in range(len(nums)+1):
            result ^= i
        for num in nums:
            result ^= num
        return result

        ###########################################