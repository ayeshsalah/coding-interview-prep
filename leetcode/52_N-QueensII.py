# Leetcode
# 52. N-Queens II
# https://www.youtube.com/watch?v=nalYyLZgvCY


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0
        visited_cols = set()
        positive_diagonal = set()
        negative_diagonal = set()

        def back_track(r):
            # base case, when row counter has reached the last row in the board
            if r == n:
                self.result += 1
                return 
            # failure cases, is column is already in visited OR
            # row and column are in the already visited positive diagonal or negative diagonal
            for c in range(n):
                if c in visited_cols or (r+c) in positive_diagonal or (r-c) in negative_diagonal:
                    continue
                visited_cols.add(c)
                positive_diagonal.add(r+c)
                negative_diagonal.add(r-c)
                back_track(r+1)
                visited_cols.remove(c)
                positive_diagonal.remove(r+c)
                negative_diagonal.remove(r-c)
        back_track(0)
        return self.result
