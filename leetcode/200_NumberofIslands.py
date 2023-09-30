# Leetcode
# 200. Number of Islands
# https://www.youtube.com/watch?v=pV2kpPD66nE

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
                new_r = row+dr
                new_c = col+dc
                if (new_r in range(rows)) and new_c in range(cols) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))
