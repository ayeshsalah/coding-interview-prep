# Leetcode
# 502. IPO
# https://www.youtube.com/watch?v=1IUzNJ6TPEM


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = [] # max heap to store the profits 
        min_capital = [(c, p) for c, p in zip(capital, profits)] # maybe we can afford this projects later 
        heapq.heapify(min_capital) # python's implementation of heap is min heap, also what we want for capital

        for i in range(k):
            # check if minimum capital is less than current capital
            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                # add profit to max heap of profits; mutiply with -1 to use as Max heap.
                heapq.heappush(max_profit, -1 * p)
            # Pop max profit and add to current capital
            if max_profit:
                w += -1 * heapq.heappop(max_profit)

        return w
