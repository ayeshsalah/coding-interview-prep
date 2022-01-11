# Leetcode
# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        heap = []
        counter = collections.Counter(s)
        for alpha, freq in counter.items():
            #  store (frequency, key) pairs in heap. Heap will be sorted based on frequency.
            #  multiply frequency with -1, this will make the elements with the highest freq as the smallest in the heap.
            heapq.heappush(heap, (-1 * freq, alpha))
        
        while heap:
            item = heapq.heappop(heap)
            for _ in range(abs(item[0])):
                result.append(item[1])
            
        return "".join(result)
