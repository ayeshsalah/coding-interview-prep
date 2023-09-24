# Leetcode
# 236. Lowest Common Ancestor of a Binary Tree
# https://www.youtube.com/watch?v=_-QHfMDde90

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return None at end of the tree
        if not root:
            return None
        # if one of the targets is foudn, return them. 
        if root == p or root == q:
            return root
        # look in the left sub tree
        left_res = self.lowestCommonAncestor(root.left, p, q)
        # look in the right sub tree
        right_res = self.lowestCommonAncestor(root.right, p, q)
        # if not found in left subtree, must be in right sub tree.
        if not left_res:
            return right_res
        # if not found in right subtree, must be in left sub tree.
        elif not right_res:
            return left_res
        # if found in both, then it the LCA.
        else:
            return root
