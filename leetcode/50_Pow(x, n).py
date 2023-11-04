# Leetcode
# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/solutions/735170/python3-solution-with-a-detailed-explanation/
# https://www.youtube.com/watch?v=g9YQyYi4IQQ


class Solution:
    def myPow(self, x: float, n: int) -> float:

        result = self.recursive_pow(x, abs(n))
        return result if n >= 0 else 1/result

    def recursive_pow(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        temp_result = self.recursive_pow(x, n//2)
        if n%2 == 0:
            return temp_result * temp_result
        else:
            return x * temp_result * temp_result
