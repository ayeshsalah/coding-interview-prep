# Leetcode
# 202. Happy Number
# https://www.youtube.com/watch?v=ljz85bxOYJ0


class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sum_of_squares(n)
            if n == 1:
                return True
        return False

    def sum_of_squares(self, n):
        result = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            result += digit
            n = n //10
        return result
