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
        
    def branch_sum(self, root, target):
        # subtract current root.val from target at every step i.e. new_target
        # if root.val and target match at the leaf level then targetSum is found.
        if not root:
            return []
        new_target = target-root.val
        if not root.left and not root.right and root.val == target:
            return True
        return self.branch_sum(root.left, new_target) or self.branch_sum(root.right, new_target)    
