# Leetcode
# 173. Binary Search Tree Iterator
# https://www.youtube.com/watch?v=RXy5RzGF5wo

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # add all left nodes to stack
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # since next() call will always be valid, just pop stack and return val.
        node = self.stack.pop()
        # append right node to stack
        right_node = node.right
        # if right node is valid, then add any left nodes to stack.
        while right_node:
            self.stack.append(right_node)
            right_node = right_node.left
        return node.val      
        
    # returns boolean, whether we have a next element
    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()