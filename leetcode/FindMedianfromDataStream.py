# Leetcode
# 295. Find Median from Data Stream
# https://www.youtube.com/watch?v=itmhHWaHupI


class MedianFinder:

    def __init__(self):
        # two heaps
        self.small = [] # max heap; Python has minheap. Elements will be multipied by -1 to create the effect of max heap.
        self.large = [] # min heap
        
    def addNum(self, num: int) -> None:
        # add every num to small heap
        heapq.heappush(self.small, (-1 * num))
        
        # check if nums in small heap are smaller than the nums in large heap
        if (self.small and self.large and 
           (-1 * self.small[0]) > self.large[0]):
            value = (-1 * heapq.heappop(self.small))
            heapq.heappush(self.large, value)
        
        # check for uneven size; the size diff betwenn small and large should not exceed 1
        if len(self.small) > len(self.large)+1:
            value = (-1 * heapq.heappop(self.small))
            heapq.heappush(self.large, value)
        if len(self.large) > len(self.small)+1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, (-1 *value))


    def findMedian(self) -> float:
        # if unequal lengths of small and large heaps, return the extra element from the longer heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]        
        
        return ((-1 * self.small[0]) + self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()