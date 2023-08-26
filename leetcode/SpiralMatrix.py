# Leetcode
# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        
        top, left = 0, 0 
        bottom, right = height-1, width-1
        spiral_order = []
        
        while top < bottom and left < right:
            
            # left to right
            for i in range(left, right+1):
                spiral_order.append(matrix[top][i])
            top +=1
            
            # right to bottom
            for i in range(top, bottom+1):
                spiral_order.append(matrix[i][right])            
            right-=1
            
            # bottom to left
            for i in range(right, left-1, -1):
                spiral_order.append(matrix[bottom][i])              
            bottom -=1
            
            # bottom to top
            for i in range(bottom, top-1, -1):
                spiral_order.append(matrix[i][left])           
            left +=1
            
        # check for single square
        if left == right == top == bottom:
            spiral_order.append(matrix[top][left])
        # check for horizontal line
        elif top == bottom:
            for i in range(left, right+1):
                spiral_order.append(matrix[top][i])
        # check for vertical line
        elif left == right:
            for i in range(top, bottom+1):
                spiral_order.append(matrix[i][left])
                         
        return spiral_order
