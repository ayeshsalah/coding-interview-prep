# Leetcode
# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_triangle = []
        for row in range(rowIndex+1):
            if row == 0:
                pascal_triangle.append([1])
            else:
                temp= [1] # first element
                for index in range(1, row):
                    temp.insert(index, pascal_triangle[row-1][index-1]+pascal_triangle[row-1][index])
                temp.append(1) # last element
                pascal_triangle.append(temp)
        # return last row of pascal's triangle 
        return pascal_triangle[-1]
