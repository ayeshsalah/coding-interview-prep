# Leetcode
# 59. Spiral Matrix II

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        top, left = 0, 0 
        bottom, right = n-1, n-1
        
        result = [[0]* n for _ in range(n)]

        num = 1
        
        while top<=bottom and left<=right:
            
            # left to right 
            for i in range(left, right+1):
                # same list, different indices
                result[top][i] = num 
                num+=1
            top+=1
            
            # top to bottom
            for j in range(top, bottom+1):
                # different list, same index
                result[j][right] = num
                num+=1
            right-=1
            
            # right to left; # reverse range 
            for k in range(right, left-1, -1): 
                # same list, different indices
                result[bottom][k] = num
                num+=1
            bottom-=1
            
            # bottom to top; # reverse range 
            for l in range(bottom, top-1, -1): 
                # different list, same index
                result[l][left] = num
                num+=1
            left+=1
            
        return result
