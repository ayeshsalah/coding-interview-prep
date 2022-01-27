# Leetcode 
# 572. Subtree of Another Tree
# https://www.youtube.com/watch?v=E36O5SWp-LE


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is None; 1. It is child of the leaf node of the root or 2. root is also None, the trees match
        if not subRoot:
            return True
        # if subRoot exists and root is None, return False
        if subRoot and not root:
            return False
        # check if root and subRoot are same tree
        if self.is_same_tree(root, subRoot):
            return True
        # call isSubTree recursively  on left sub tree with subRoot and right sub tree with SubRoot
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
        
    # Same solution as Leetcode 100
    def is_same_tree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if tree1 and tree2 and tree1.val == tree2.val:
            return (self.is_same_tree(tree1.left, tree2.left) and self.is_same_tree(tree1.right, tree2.right))
        return False
