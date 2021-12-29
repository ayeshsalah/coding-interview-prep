# Leetcode
# 43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str( self.covert_to_unicode(num1) * self.covert_to_unicode(num2))
    
    def covert_to_unicode(self, string):
        result = 0
        for num in string:
            result = result * 10 + (ord(num)-ord('0'))
        return result
