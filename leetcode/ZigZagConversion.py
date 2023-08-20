#LeetCode
#6. ZigZag Conversion
# https://www.youtube.com/watch?v=Q2Tw6gcVEwc

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Formula for first and last row: (numRows-1) * 2
        Formula for middle rows: i + ((numRows-1) * 2 ) - 2*r
        """
        if numRows == 1: 
            return s

        result = ""
        for r in range(numRows):
            increment = (numRows-1) * 2
            for i in range(r, len(s), increment):
                result += s[i] # for first and last row
                # check if we are in middle rows
                if r != 0 and r != numRows-1:
                    # check if middle rows increment is inbounds
                    if i+increment-(2*r) < len(s):
                        result += s[i+increment-(2*r)]        
        return result
