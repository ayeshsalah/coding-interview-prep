# Leetcode
# 417. Pacific Atlantic Water Flow
# https://www.youtube.com/watch?v=s-VkcjHqkGI


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        def dfs(row, col, visited, prev_height):
            if (row >= rows or col >= cols or       # out of bounds on right
            row < 0 or col < 0 or                   # out of bounds on left
            (row, col) in visited or                # already in visited
            heights[row][col] < prev_height):       # lesser than prev_height
                return 
            # add new cell to visited
            visited.add((row, col))
            # run dfs in all 4 directions
            dfs(row+1, col, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])
        
        # store all the cells that can reach pacific and atlanic
        pacific = set()
        atlantic = set()
        
        # find all the cells reachable from pacific starting at the top row and
        # all cells reachable by atlantic starting from bottom row
        # to start off pass the value of the cell in place of previous height 
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])    
            dfs(rows-1, c, atlantic, heights[rows-1][c])
            
        # find all the cells reachable from pacific start from left column and 
        # all cells reachable from atlantic starting from right column
        # to start off pass the value of the cell in place of previous height 
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r, c])
        
        return result
