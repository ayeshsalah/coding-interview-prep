# Leetcode
# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We can make use of the product of all the numbers to the left and all the numbers to the right of the index. 
        # Multiplying these two individual products would give us the desired result. ##
        # ==> left product [1,2,3,4] ==> [1,1,2,6] (left to right)
        # ==> right product [1,2,3,4] ==> [24,12,4,1] (right to left)
        # ==> multiplying these two will get answer.
        
        length = len(nums)
        left_prods = [1] * length
        right_prods = [1] * length
        result = []
        for i in range(1, length):
            left_prods[i] = nums[i-1] * left_prods[i-1]
            right_prods[length-i-1] = nums[length-i] * right_prods[length-i]
        print(left_prods)
        print(right_prods)
        
        for i in range(length):
            result.append(left_prods[i] * right_prods[i])
        return result
