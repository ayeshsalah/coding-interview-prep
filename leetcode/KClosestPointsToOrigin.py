# Leetcode
# 973. K Closest Points to Origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for x, y in points:
            diff = pow(x-0, 2) + pow(y-0, 2)
            heapq.heappush(heap, (diff, [x, y]))
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
