# Leetcode
# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_price = inf
        for price in prices:
            max_profit = max(max_profit, price-min_price) # calculate profit at every iteration and store the highest
            min_price= min(min_price, price) #find lowest price
        return max_profit

#### Addtional Solution ####

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            max_profit = max(max_profit, (prices[right] - prices[left]))
        return max_profit
