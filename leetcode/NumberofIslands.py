# Leetcode
# 200. Number of Islands
# https://www.youtube.com/watch?v=pV2kpPD66nE

#TODO Add explanation
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    self.bfs(grid, r, c, visited)
        return islands
    
    def bfs(self, grid, r, c, visited):
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r = row+dr
                c = col+dc
                if (r in range(rows)) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r,c))
