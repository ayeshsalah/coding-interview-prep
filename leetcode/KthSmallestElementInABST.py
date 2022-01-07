# Leetcode
# 230. Kth Smallest Element in a BST
# https://www.youtube.com/watch?v=5LUXSvjmGCw and check first comment for correction in the code.
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/693879/Python-2-Solutions-Iterative-and-recursive-with-explanation


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # store the left nodes in a stack.
        # when you reach a leaf node. pop the stack and check the right node. 
        stack = []
        count = 0
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            count += 1
            if count == k:
                return root.val
            root = root.right
