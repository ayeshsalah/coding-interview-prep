# Leetcode
# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBST(nums, 0, len(nums)-1)
        
    def buildBST(self, array, left, right):
        if left == right:
            return TreeNode(array[left])
        elif left < right:
            middle = (left+right)//2
            new_node = TreeNode(array[middle])
            new_node.left = self.buildBST(array, left, middle-1)
            new_node.right = self.buildBST(array, middle+1, right)
            return new_node
