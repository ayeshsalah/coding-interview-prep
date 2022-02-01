# Leetcode
# 73. Set Matrix Zeroes
# https://www.youtube.com/watch?v=T41rL0L3Pnw


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # use row_zero to determine if first element of row 0 needs to be zeroed. 
        row_zero = False 
        # find the rows and cols to be zeroed
        for i in range(rows):
            for j in range(cols):
                # if zero is found in matrix
                # set the corresponding row/col in first row/col to 0.
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    # check if i is the first element of row 0.
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True
                        
        # Using the first row/col, zero out the corresponding rows/cols.
        for r in range(1, rows):
            for c in range(1, cols) :
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # check if first col needs to be zeroed
        if matrix[0][0] == 0:
            for r in range(1, rows):
                matrix[r][0] = 0
                
        # check if first row needs to be zeroed
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
