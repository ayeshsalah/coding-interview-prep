# Leetcode
# 1557. Minimum Number of Vertices to Reach All Nodes

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        left = set()
        right = set()
        for l, r in edges:
            left.add(l)
            right.add(r)
        return list(left.difference(right))
