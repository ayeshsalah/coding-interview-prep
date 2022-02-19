# Leetcode
# 1143. Longest Common Subsequence
# https://www.youtube.com/watch?v=Ua0GhsJSlWM


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom up DP
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    # 1 + the diagonal value
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # max of value at the right and bottom
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # print(dp)
        return dp[0][0]
