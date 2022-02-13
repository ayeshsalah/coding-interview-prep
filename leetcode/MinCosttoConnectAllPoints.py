# Leetcode 
# 1584. Min Cost to Connect All Points

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Minimum Spanning Tree (MST) using Kruskal's Algorithm    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        size = len(points)
        edges = []
        for i in range(size):
            for j in range(i+1, size):
                # print(points[i])
                # print(points[j])
                distance = self.find_manhattan_dsitance(points[i], points[j])
                # print(distance)
                # edges.append((distance, (tuple(points[i])), tuple(points[j])))
                edges.append((distance, i, j))
                
        # Use heapq to sort the items by distance. heappop returns the smallest distance. 
        heapq.heapify(edges)
        # print(edges)
        

        disjoint_set = UnionFind(size)
        result = 0 
        count = size-1 # count of edges in MST(minimum spanning tree) will be no. of vertices minus 1. 
        # Use disjoint set to check if points are connected.
        # if they are not connected add the distance to result, decrement count and union the 2 points.
        while edges and count > 0:
            edge = heapq.heappop(edges)
            if not disjoint_set.connected(edge[1], edge[2]):
                result += edge[0]
                count -= 1
                disjoint_set.union(edge[1], edge[2])
        return result               
        
    def find_manhattan_dsitance(self, x, y):
        return abs(x[0]-y[0]) + abs(x[1]-y[1])
