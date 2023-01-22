# Leetcode
# 239. Sliding Window Maximum
# Refer: https://www.geeksforgeeks.org/deque-in-python/
# https://leetcode.com/problems/sliding-window-maximum/solutions/871317/clear-thinking-process-with-picture-brute-force-to-mono-deque-python-java-javascript/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # store indices
        result = []

        for i, num in enumerate(nums):
            # maintain a monotonic array
            # check if smaller elements exists. Pop all smaller elements, then append new element. 
            while q and nums[q[-1]]<num:
                q.pop()
            q.append(i)

            # check if left is still inbounds, if not remove from left
            if q[0] <= i-k:
                q.popleft()

            # if window is size k, then add to result array
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
