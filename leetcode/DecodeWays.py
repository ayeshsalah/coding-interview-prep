# Leetcode
# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)
# https://leetcode.com/problems/decode-ways/discuss/30540/Very-very-very-simple-Python-solution-using-Top-down-DP

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        return self.decode(s, dp)
    
    def decode(self, s, dp):
        # check if string in dp 
        if s in dp:
            return dp[s]
        # if first char is 0 then no pattern can be created return 0
        if len(s)>0 and s[0] == '0':
                return 0
        # if empty string or length is 1 return 1
        if s == "" or len(s) == 1:
            return 1   
        # int of first 2 chars is less then 26 then call self.decode for first char and second char 
        # store the result in dp
        if int(s[:2])<=26:
            first = self.decode(s[1:], dp)
            second = self.decode(s[2:], dp)
            dp[s] = first+second
            return first+second
        # else call self.decode with fist char and store in dp
        else:
            first = self.decode(s[1:], dp)
            dp[s] = first
            return first
