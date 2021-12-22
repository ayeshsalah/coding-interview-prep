# Leetcode
# 98. Validate Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root, float("-inf"), float("inf"))
    
    def validateBST(self, root, min_val, max_val):
        if root:
            # if current value is greater then left OR lesser then right -> Invalid BST
            if not (min_val < root.val < max_val):
                return False
            return self.validateBST(root.left, min_val, root.val) and self.validateBST(root.right, root.val, max_val)
        # Return true if the empty leaf node is reached without returning False
        return True
