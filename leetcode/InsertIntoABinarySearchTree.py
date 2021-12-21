# Leetcode
# 701. Insert into a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If empty node then return TreeNode with val
        if not root:
            return TreeNode(val)
        # If value is greater than the root of BST, insert in right node.
        if val > root.val:
            # Check if root.right exists. 
            # Recursively insertINtoBST, if root.right exists.
            # Add root.right if it does not exist. 
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        # If value is less than the root of BST, insert in left node.
        else:
            # Check if root.left exists. 
            # Recursively insertIntoBST, if root.left exists.
            # Add root.left if it does not exist. 
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        return root
