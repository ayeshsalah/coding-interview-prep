# Leetcode
# 222. Count Complete Tree Nodes
# https://www.youtube.com/watch?v=JxIf7Rs9nPw


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Find the count of the left nodes to find the height of the tree.
        left_count = self.count_left(root)
        # Find the count of the right nodes to find if the height equals to left, i.e., the tree is balanced.
        right_count = self.count_right(root)


        # if left > right, tree is not balanced. No need to check right > left as, left is filled in for "complete" binary trees. 
        if left_count > right_count:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
        else:
            # tree is balanced, find number of nodes using the formula (2 ** h) - 1
            return (2**left_count)-1


    # count left
    def count_left(self, node):
        if not node:
            return 0
        return self.count_left(node.left) + 1

    # count right 
    def count_right(self, node):
        if not node:
            return 0
        return self.count_right(node.right) + 1
