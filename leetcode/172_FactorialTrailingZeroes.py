# Leetcode
# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/solutions/522315/clear-explanation-of-the-solution-since-i-didn-t-find-an-adequate-one/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0 
        while n!=0:
            n = n//5
            result += n
        return result
