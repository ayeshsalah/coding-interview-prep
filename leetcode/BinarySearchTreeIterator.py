# Leetcode
# 173. Binary Search Tree Iterator
# https://www.youtube.com/watch?v=D2jMcmxU4bs

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # returns the next smallest number
    def next(self) -> int:
        node = self.stack.pop()
        right_node = node.right
        while right_node:
            self.stack.append(right_node)
            right_node = right_node.left
        return node.val      
        
    # returns boolean, whether we have a next smallest number
    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()