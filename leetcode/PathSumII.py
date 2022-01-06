# Leetcode
# 113. Path Sum II

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.branch_sum(root, targetSum, [], [])
    
    def branch_sum(self, root, target, temp_list, result):
        # use temp_list to store the current path to the leaf node
        # subtract current root.val from target at every step i.e. new_target
        # if root.val and target match at the leaf level then targetSum is found then append temp_list to result
        # temp_list[:] is used to force call by value; it sends a shallow copy of the temp_list instead of the reference. 
        # call by reference will not have the correct values for left and right.
        if not root:
            return []
        temp_list.append(root.val)
        new_target = target-root.val
        if not root.left and not root.right and root.val == target:
            result.append(temp_list)
        if root.left:
            self.branch_sum(root.left, new_target, temp_list[:], result) 
        if root.right:
            self.branch_sum(root.right, new_target, temp_list[:], result)
        return result
