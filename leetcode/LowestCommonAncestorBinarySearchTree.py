# Leetcode
# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_val = root.val
        # Both p and q are smaller than current node, then search left-subtree by recursive
        if current_val > p.val and current_val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # Both p and q are larger than current node, then search right-subtree by recursive
        elif current_val < p.val and current_val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # Both p and q are not on the same side of current node, then current node must be the Lowest common ancestor of ( p, q )
        # Constraints mentions, p and q will exist in the BST. So need to check edge cases. 
        else:
            return root
