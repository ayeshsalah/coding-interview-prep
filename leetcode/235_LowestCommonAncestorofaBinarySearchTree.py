# Leetcode
# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # Both p and q are larger than root, then search right-subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # Both p and q are smaller than root, then search left-subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # Both p and q are not on the same side of root, then root must be the Lowest common ancestor of ( p, q )
            # Constraints mentions, p and q will exist in the BST. So no need to check edge cases. 
            else:
                return root
