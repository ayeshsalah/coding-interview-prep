# Leetcode
# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/1567849/Python-or-Prefix-Sum-Beats-99-or-Simplest-and-Efficient-Solution-With-Explaination

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cummulative_sum = 0
        hashmap = {}
        subarray_count = 0
        for num in nums:
            cummulative_sum += num
            if cummulative_sum == k:
                subarray_count += 1
            if cummulative_sum - k in hashmap:
                subarray_count += hashmap[cummulative_sum - k]
 
            hashmap[cummulative_sum] = hashmap.get(cummulative_sum, 0) +1
        return subarray_count

