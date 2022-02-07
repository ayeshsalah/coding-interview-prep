# Leetcode
# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/discuss/923039/Union-Find-with-union-by-ranks-and-path-compression


class UnionFind:
    def __init__(self, size):
        self.vertices = [i for i in range(size)]
        self.rank = [1] * size
        self.groups = size
        
    def find(self, item):
        if item == self.vertices[item]:
            return item
        self.vertices[item] = self.find(self.vertices[item])
        return self.vertices[item]
    
    def union(self, vertex1, vertex2):
        v1 = self.find(vertex1)
        v2 = self.find(vertex2)
        if v1 != v2:
            if self.rank[v1] > self.rank[v2]:
                self.vertices[v2] = v1
            elif self.rank[v2] > self.rank[v1]:
                self.vertices[v1] = v2
            else:
                self.rank[v1] +=1
                self.vertices[v2] = v1

            self.groups -= 1

    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        
        n=len(isConnected)
        disjoint_set = UnionFind(n)
        
        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 1:
                    disjoint_set.union(r, c)
        return disjoint_set.groups
