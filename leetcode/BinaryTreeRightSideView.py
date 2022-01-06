# Leetcode
# 199. Binary Tree Right Side View

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Building on the solution for LevelOrderTraversal (leetcode #102)
        # Appending only the last element of every level.
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
            result.append([item.val for item in current][-1])
            current = next_level
        return result
