# Leetcode
# 79. Word Search
# Backtracking solution with O(n * m* 4^n)
# https://www.youtube.com/watch?v=pfiQ_PS1g8E


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        visiting = set()
        
        def dfs(row, column, current_index):
            # base case
            if current_index == len(word):
                return True
            # failure cases
            if (row < 0 or column < 0 or 
                row >= rows or column >= columns or 
                word[current_index] != board[row][column] or
                (row, column) in visiting):
                return False
            # add to visiting
            visiting.add((row, column))
            # move to adjacent cells
            result = (dfs(row+1, column, current_index+1) or
                      dfs(row-1, column, current_index+1) or
                      dfs(row, column+1, current_index+1) or
                      dfs(row, column-1, current_index+1))
            # remove from visiting as we are returning the function and not visiting the cell anymore.
            visiting.remove((row, column))
            return result
        
        # grid search 
        for row in range(rows):
            for col in range(columns):
                if dfs(row, col, 0):
                    return True
        return False
