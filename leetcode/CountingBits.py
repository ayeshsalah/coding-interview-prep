# Leetcode
# 338. Counting Bits
# https://www.youtube.com/watch?v=RyBM56RIWrM

class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n) time & O(n) space
        dp = [0] * (n+1)
        offset = 1 # multiple of 2 
        
        for num in range(1, n+1):
            # check if offset( the current power of 2) is the same as the num, if yes update offset to num.
            if offset * 2 == num:
                offset = num
            dp[num] = 1 + dp[num-offset]
            
        return dp
