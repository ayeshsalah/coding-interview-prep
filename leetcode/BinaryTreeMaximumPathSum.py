# Leetcode
# 124. Binary Tree Maximum Path Sum
# https://www.youtube.com/watch?v=Hr5cWUld4vU


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]
        self.inorder_recursive(root, result)
        return result[0]
    
    def inorder_recursive(self, root, result):
        if root:
            left_result = self.inorder_recursive(root.left, result)
            right_result = self.inorder_recursive(root.right, result)
            # handle negative values by getting max between result and 0.
            left_result = max(left_result, 0)
            right_result = max(right_result, 0)
            # max path sum with split
            result[0] = max(result[0], (root.val+left_result+right_result))
            # return path sum without split
            return root.val + max(left_result, right_result)
        else:
            return 0
