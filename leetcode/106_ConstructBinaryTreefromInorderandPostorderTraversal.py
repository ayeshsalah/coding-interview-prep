# Leetcode
# 106. Construct Binary Tree from Inorder and Postorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        # use the last node of postorder as the root; pop the element used to create new node.             
        root = postorder.pop()
        # find the index of the root node in inorder and split inorder list based on the root index
        root_index = inorder.index(root)
        tree = TreeNode(root)
        # build right before left
        # use right+1 to build right
        tree.right = self.buildTree(inorder[root_index+1:], postorder)
        tree.left = self.buildTree(inorder[:root_index], postorder)
        return tree
    