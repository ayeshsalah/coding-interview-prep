# Leetcode
# 190. Reverse Bits
# https://www.youtube.com/watch?v=UcoN6UjAI64
# TODO add explanation 

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res
