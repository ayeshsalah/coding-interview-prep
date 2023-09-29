# Leetcode
# 530. Minimum Absolute Difference in BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        diff = float("inf")
        previous = float("-inf")
        current = root
        stack = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            diff = min(diff, node.val-previous)
            previous = node.val
            current = node.right
        return diff
