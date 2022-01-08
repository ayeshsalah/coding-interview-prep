# Leetcode
# 236. Lowest Common Ancestor of a Binary Tree
# https://www.youtube.com/watch?v=_-QHfMDde90

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        
        # Find p or q in left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        # Find p or q in right subtree
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left:
            return right
        elif not right:
            return left
        # If p and q found in left and right subtree of this node, then this node is LCA
        else:
            return root
