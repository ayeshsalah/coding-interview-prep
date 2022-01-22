# Leetcode
# 371. Sum of Two Integers
# https://www.youtube.com/watch?v=gVUrDV4tZfY
# https://leetcode.com/problems/sum-of-two-integers/discuss/699379/Python-Simple-bit-operations-solution-with-detailed-explanation

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
        while(b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a