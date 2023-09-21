# Leetcode
# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.branch_sum(root, targetSum)

    def branch_sum(self, node, target):
        if not node:
            return None
        # subtract current node.val from target at every step.
        # if target is 0, at the leaf level then targetSum is found.
        target -= node.val
        if node.left == None and node.right == None and target == 0:
            return True
        return self.branch_sum(node.left, target) or self.branch_sum(node.right, target)
