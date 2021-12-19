# Leetcode
# 102. Binary Tree Level Order Traversal
# TODO Recursive Solution 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level is a list of the nodes in the current level. 
        # Keep appending a list of the values of these nodes to result 
        # Update level with all the nodes in the next level (kids) until it reaches an empty level. 
        level = [root]
        result = []
        while root and level:
            current = []
            next_level = []
            for node in level:
                current.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(current)
            level = next_level
        return result
