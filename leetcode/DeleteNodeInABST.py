# Leetcode
# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/discuss/887303/Python-3-greater-97.55-faster.-Explanation-added

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # First find the node that we need to delete.
        # After it's found, think about ways to keep the tree BST after deleting the node.
        # If there's no left or right subtree, we found the leaf. Delete this node without any further traversing.
        # If it's not a leaf node, We can either replace the delete node with the minimum from the right subtree (if right exists) or 
        # we can replace the delete node with the maximum from the left subtree (if left exists).
        # also delete the minimum or the maximum from the subsequent tree. 
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val == key:
            # Node to be deleted is leaf node. Set eh value to None
            if not root.left and not root.right:
                root = None
            # Node has a right child. Find the min in right nodes, assign it inplace of deleted node and delete it from it's original place.
            elif root.right:
                root.val = self.find_right_min(root.right)
                root.right = self.deleteNode(root.right, root.val)
            # Node has a left child. Find the max in left nodes, assign it inplace of deleted node and delete it from it's original place.                
            elif root.left:
                root.val = self.find_left_max(root.left)
                root.left = self.deleteNode(root.left, root.val)
        return root
            
    def find_right_min(self, right_tree):
        # the lowest in the right tree would be in the left nodes.
        while right_tree.left:
            right_tree = right_tree.left
        return right_tree.val
        
    def find_left_max(self, left_tree):
        # the highest in the left tree would be in the right nodes.
        while left_tree.right:
            left_tree = left_tree.right
        return left_tree.val
