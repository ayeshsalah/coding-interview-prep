# Leetcode
# 322. Coin Change
# https://www.youtube.com/watch?v=H9bfqozjoqs
# DP bottom Up approach

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Values in this array equal the number of coins needed to achieve the cost of the index
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # Loop through every needed amount
        for amt in range(amount + 1):
            # Loop through every coin value
            for coin in coins:
                # Check that the coin is not bigger than the current amount
                if coin <= amt:
                    # dp[amt]: number of coins needed to make amount amt
                    # dp[amt-coin]: number of coins needed to make the amount before adding the current coin to it (+1 to add the current coin)
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        
        # Check if any combination of coins was found to create the amount
        if dp[amount] == amount + 1:
            return -1
        
        # Return the optimal number of coins to create the amount
        return dp[amount]        
