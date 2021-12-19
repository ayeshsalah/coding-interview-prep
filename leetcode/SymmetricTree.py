# Leetcode
# 101. Symmetric Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.checkSymmetery(root.left, root.right)
        
    def checkSymmetery(self, left_n, right_n):
        if left_n and right_n:
            return left_n.val == right_n.val and self.checkSymmetery(left_n.left, right_n.right) and self.checkSymmetery(left_n.right, right_n.left)
        return left_n == right_n
