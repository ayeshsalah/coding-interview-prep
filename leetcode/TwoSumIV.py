# Leetcode
# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = {}
        return self.traverseBST(root, visited, k)
        
    def traverseBST(self, node, visited,target):
        if node:
            diff = target-node.val
            if diff in visited:
                return True
            visited[node.val] = visited.get(node.val+1, 1)
            return self.traverseBST(node.left, visited, target) or self.traverseBST(node.right, visited, target)
        return False
