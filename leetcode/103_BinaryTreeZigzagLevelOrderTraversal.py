# Leetcode
# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Building on the solution for LevelOrderTraversal (leetcode #102)
        # Added level_counter to keep track of levels
        # Reverse the list for even levels. So items are added right to left instead of left to right. 
        # If next_level has nodes, increment level_counter 
        if not root:
            return []
        level_counter = 1
        current = [root]
        result = []
        while current:
            next_level = []
            for node in current:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level_counter %2 == 0: 
                current.reverse()
            result.append([item.val for item in current])
            current = next_level
            if next_level:
                level_counter +=1
        return result
