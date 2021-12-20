# Leetcode
# 112. Path Sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.branchSums(root, targetSum)
        
    def branchSums(self, root, target, total=0):
        if root:
            total+=root.val
            if not (root.left or root.right) and target == total:
                return True
            return self.branchSums(root.left, target, total) or self.branchSums(root.right, target, total)
