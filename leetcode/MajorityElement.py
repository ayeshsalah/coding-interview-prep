# Leetcode
# 169. Majority Element
# Boyer-Moore Majority Vote Algorithm
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[0][0]
