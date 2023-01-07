# Leetcode
# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = set()
        left = 0
        right = len(numbers)-1
        while left <= right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
