# Leetcode
# 1405. Longest Happy String
# https://www.youtube.com/watch?v=8u-H6O_XQKE


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # greedy approach with maxHeap
        result = ""
        max_heap = []
        # use a min heap with negative values to get an effective max heap
        # add the count of each char
        # pop the largest char and build the happy string 
        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count > 0:
                heapq.heappush(max_heap, ( (-1 * count), char) )
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            # check if last 2 chars are same as the current char
            if len(result) > 1 and result[-1] == result[-2] == char:
                # check if there are any elements in max heap; if no element remains break
                if not max_heap:
                    break
                # there are elements in max_heap, get the 2nd item in the heap 
                count2, char2 = heapq.heappop(max_heap)
                result += char2 # increasing count as we store negative in max_heap, we want to reach 0.
                count2 += 1
                if count2:
                    heapq.heappush(max_heap, (count2, char2))
            else:
                result += char 
                count += 1 # increasing count as we store negative in max_heap, we want to reach 0.
            # check count and do a heappush irrespective of the if else condition. if count has a value > 0 it has to go back into the heap.
            if count:
                heapq.heappush(max_heap, (count, char))
        return result
