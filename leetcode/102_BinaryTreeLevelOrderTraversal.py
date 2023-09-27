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
        # current is a list of the nodes in the current level. 
        # for every node in current, if there is left or right, append it to next_level
        # append val of nodes in current to result
        # assign next_level to current 
        if not root:
            return []
        current = [root]
        result = []
        while current:
            next_level = []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append([item.val for item in current])
            current = next_level
        return result
                    