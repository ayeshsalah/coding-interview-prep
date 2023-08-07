# Leetcode
# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # start from index 1. Compare current and previous value. 
        # if current > previous, add the difference to profit.
        profit = 0 
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i]-prices[i-1])
        return profit
