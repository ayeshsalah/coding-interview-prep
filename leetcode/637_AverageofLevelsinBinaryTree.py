# Leetcode
# 637. Average of Levels in Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # based on level order travesal of Binary Tree (Leetcode #102)
        if not root:
            return []
        result = []
        current = [root]
        while current:
            next_nodes = []
            for node in current:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            curr_vals = [i.val for i in current]
            avg = sum(curr_vals)/len(current)
            result.append(avg)
            current = next_nodes
        return result
