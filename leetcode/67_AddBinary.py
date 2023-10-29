# Leetcode
# 67. Add Binary


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # binary addition rules 
        # 0 + 0 = 0
        # 1 + 0 = 1
        # 1 + 1 = 0 (carry 1)
        # 1 + 1 + (carry 1) = 1 (carry 1)
        # Trick:
        # Result digit = (a_digit + b_digit + carry) % 2
        # Carry digit = (a_digit + b_digit + carry) // 2
        a_len = len(a) * -1 # mutiple by -1 to get negative index
        b_len = len(b) * -1
        carry = 0 
        result = ""
        current = -1
        while current >= a_len or current >= b_len:
            a_digit = int(a[current]) if current >= a_len else 0
            b_digit = int(b[current]) if current >= b_len else 0

            res = (a_digit + b_digit + carry) % 2
            result = str(res) + result
            carry = (a_digit + b_digit + carry) // 2
            current -= 1
        
        if carry: 
            result = "1" + result
        return result
