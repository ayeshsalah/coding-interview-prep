# Leetcode
# 130. Surrounded Regions
# https://www.youtube.com/watch?v=9z2BunfoZ5Y

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        # Run DFS to Capture unsurrounded region on the border of the board. Convert O to T (Temp)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    self.dfs(board, rows, cols, r, c)

        # Capture surrounded regions. Convert any remaining O to X.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Uncapture unsurrounded regions. Convert T to O.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"        

    def dfs(self, board, rows, cols, r, c):
        # base case check if r and c are with in bounds and value is O.
        if (r < 0 or 
            c < 0 or
            r == rows or
            c == cols or 
            board[r][c] != "O"):
            return
        # set O -> T
        board[r][c] = "T"
        # run dfs in all 4 directions
        self.dfs(board, rows, cols, r+1, c)
        self.dfs(board, rows, cols, r, c+1)
        self.dfs(board, rows, cols, r-1, c)
        self.dfs(board, rows, cols, r, c-1)
