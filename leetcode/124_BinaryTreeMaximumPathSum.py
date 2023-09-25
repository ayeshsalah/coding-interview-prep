# Leetcode
# 124. Binary Tree Maximum Path Sum
# https://www.youtube.com/watch?v=Hr5cWUld4vU


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float("-inf")
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node:
            return 0 
        # handle negative values by getting max between result and 0.
        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)
        # update the result with the max path sum with split
        self.result = max(self.result, node.val+left+right)
        # return the path value without the split.
        return node.val + max(left, right)
