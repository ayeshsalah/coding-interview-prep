# Leetcode
# 100. Same Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both trees are None, it is considered as the same tree.
        if not p and not q:
            return True
        # if trees are non null and val matches
        # recursively check if left trees of p & q and right tree of p & q match.
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        # if the above conditions did not match, return False
        return False
