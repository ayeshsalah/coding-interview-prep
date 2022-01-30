# Leetcode
# 678. Valid Parenthesis String
# https://www.youtube.com/watch?v=QhPdNS143Qg and https://github.com/neetcode-gh/leetcode/blob/main/678-Valid-Parenthesis-String.py
# TODO add explanation comments 


class Solution:
    # DP solution with O(n^2) time 
    def checkValidString(self, s: str) -> bool:
        dp = { (len(s), 0): True} # key = (i, left_parenthesis_count) -> is_valid
        return self.dfs(s, dp, 0, 0)
    
    def dfs(self, s, dp, index, left_count):
        if len(s) == index or left_count < 0:
            return left_count == 0
        if (index, left_count) in dp:
            return dp[(index, left_count)]
        if s[index] == "(":
            dp[(index, left_count)] = self.dfs(s, dp, index+1, left_count+1)
        elif s[index] == ")":
            dp[(index, left_count)] = self.dfs(s, dp, index+1, left_count-1)
        else:
            dp[(index, left_count)] = (self.dfs(s, dp, index+1, left_count+1) or # '(' case
                                       self.dfs(s, dp, index+1, left_count-1) or # ')' case
                                       self.dfs(s, dp, index+1, left_count))     # '' case
        return dp[(index, left_count)]
