# Leetcode
# 169. Majority Element
# Boyer-Moore Majority Vote Algorithm
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
# https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for n in nums[1:]:
            if count == 0:
                candidate = n            
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate
