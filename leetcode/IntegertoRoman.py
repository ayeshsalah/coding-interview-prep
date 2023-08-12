# Leetcode 
# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        mapping_list = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]
        result = ""
        for roman, integer in reversed(mapping_list):
            count = num//integer
            if count:
                result += (roman * count)
                num = num % integer
        return result
