# Leetcode
# 114. Flatten Binary Tree to Linked List
# https://www.youtube.com/watch?v=rKnD7rLT0lI


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        root = self.dfs_flatten(root)

    def dfs_flatten(self, node):
      if not node:
        return None

      left_tail = self.dfs_flatten(node.left)
      right_tail = self.dfs_flatten(node.right)
       
      # we only have to move left_tail to right, as right is already on the right. 
      if left_tail:
        left_tail.right = node.right # left child node's right becomes parent's right
        node.right = node.left # parent's right becomes parent's left. Since left's right was parent's right. We get Parent->left->right.
        node.left = None # set the left has none. 

      # we return the right tail, so the right side of the grand parent can be connected. 
      # if no right_tail, return left_tail, if no left_tail, return node.
      return right_tail or left_tail or node
