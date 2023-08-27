# Leetcode
# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0 
        right = len(matrix)-1
        while left<right:
            # i will be used to iterate thru all the rows
            for i in range(right-left):
                top = left
                bottom = right
                # save top left      
                top_left = matrix[top][left+i]
                # move bottom left into top left
                matrix[top][left+i] = matrix[bottom-i][left]
                # move bottom right to bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                # move top right to bottom right
                matrix[bottom][right-i] = matrix[top+i][right]
                # move saved top_left to top right
                matrix[top+i][right] = top_left
            left +=1
            right -= 1
