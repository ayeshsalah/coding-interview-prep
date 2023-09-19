# Leetcode
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34613/A-Python-recursive-solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # use the first node of preorder as the root; pop the element used to create new node. 
        root = preorder.pop(0)
        # find the index of the root node in inorder and split inorder list based on the root index
        root_index = inorder.index(root)
        tree = TreeNode(root)
        # build left before right
        # use right+1 to build right
        tree.left = self.buildTree(preorder, inorder[:root_index])
        tree.right = self.buildTree(preorder, inorder[root_index+1:])
        return tree
