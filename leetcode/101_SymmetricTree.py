# Leetcode
# 101. Symmetric Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      if root: 
        return self.check_symmetry(root.left, root.right)

        
    def check_symmetry(self, left_node, right_node):
      if not left_node or not right_node: # If anyone is None, return the comparison. If both are None, then True.
        return left_node == right_node
      if left_node.val != right_node.val: # If values are not same, return False
        return False
      # If both the above conditions are not met then, valid numbers, compare further.
      # Compare left_node's left with right_node's right and 
      #         left_node's right with right_node's left. 
      return self.check_symmetry(left_node.left, right_node.right) and self.check_symmetry(left_node.right, right_node.left)  
