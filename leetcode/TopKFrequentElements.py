# 347. Top K Frequent Elements
# Leetcode

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # python counter approach 
        # counter = collections.Counter(nums)
        # return [element for element, _ in counter.most_common(k)]

        ###########################################################
        # heapq solution 
        heap = []
        # by default heapq in python is min heap, i.e., heappop( pops the smallest elements.
        heapq.heapify(heap)
        result = []
        counter = collections.Counter(nums)
        for key, frequency in counter.items():
            #  store (frequency, key) pairs in heap. Heap will be sorted based on frequency.
            #  multiply frequency with -1, this will make the elements with the highest freq as the smallest in the heap.
            heapq.heappush(heap, (-1 * frequency, key))
        # return the top 'k' elements by popping from the heap 'k' times. 
        # Since we stored negative frequency, the top k elements will the elements with highest frequency. 
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
