# Leetcode
# 373. Find K Pairs with Smallest Sums
# https://www.youtube.com/watch?v=Youk8DDnLU8


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k:
            return 
        result = []
        heap = []
        visited = set()

        # add first element of nums1 and nums2 to heap
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0)) # (sum, nums1_index, nums2_index)
        visited.add((0,0))

        while k and heap:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.add((i+1, j))
            
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.add((i, j+1))
            k -= 1
        
        return result
