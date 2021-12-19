# Leetcode
# 104. Maximum Depth of Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.findMaxDepth(root, depth=0)
        
    def findMaxDepth(self, root, depth):
        if root:
            return max(self.findMaxDepth(root.left, depth+1), self.findMaxDepth(root.right, depth+1))
        return depth
