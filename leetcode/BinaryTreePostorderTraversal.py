# Leetcode
# 145. Binary Tree Postorder Traversal
# TODO Iterative Solution  

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorder_recursive(root, result)
        return result
    
    def postorder_recursive(self, root, result):
        if root:
            self.postorder_recursive(root.left, result)
            self.postorder_recursive(root.right, result)            
            result.append(root.val)
