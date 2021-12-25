# Leetcode
# 240. Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        row_num = height-1
        index = 0 
        while row_num in range(0, height) and index in range(0, width):
            if matrix[row_num][index] == target:
                return True
            elif matrix[row_num][index] > target:
                row_num -= 1
            elif matrix[row_num][index] < target:
                index += 1
        return False
