# Leetcode
# 55. Jump Game
# Greedy Approach in O(n) time 
# https://www.youtube.com/watch?v=Yan0cv2cLy8

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # inital target is the last index
        # check elements in reverse, for elements's value + element's index 
        # if the sum is greater than target, make current index the new target, i.e., the last index can reached from current index
        # at the end of the iteration if the target is 0 then all elements can reach target
        target = len(nums)-1
        for index in range(len(nums)-2, -1, -1):
            if index + nums[index] >= target:
                target = index
        return target == 0

