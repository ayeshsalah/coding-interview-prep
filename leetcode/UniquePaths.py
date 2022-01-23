# Leetcode
# 62. Unique Paths
# https://www.youtube.com/watch?v=IlEsdxuD4lY


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # since the movement is restricted to down and right
        # the bottom row and the right most column will be 1's. 
        # the remaining cell values can be calculated as the sum of the value of the right and value of the bottom
        # we can start calulating row by row starting from m-1 row and
        # col by col starting from right n-2 column
        # The value at index 0 of the top most row will have the number of unique paths.
        row = [1 for i in range(n)]
        for _ in range(m-1): 
            new_row = [1 for i in range(n)]
            for j in range(n-2, -1, -1):
                # val of new row = val of right + val of bottom row
                new_row[j] = new_row[j+1] + row[j]
            row = new_row
        return row[0]
