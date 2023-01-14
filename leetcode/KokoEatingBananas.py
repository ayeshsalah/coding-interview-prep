# Leetcode
# 875. Koko Eating Bananas


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the max eating speed can be the largest pile in piles.
        result = max(piles)
        # We can find the minimum eating speed between 1 and largest pile. 
        left = 1 
        right = max(piles)
        # Use binary search to find the minimum speed. 
        while left<=right:
            middle = (left+right)//2
            # find time taken with middle speed
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(p / middle)
            # if time is less than the h(threshold), update the minimum result and move right to middle-1.
            if time_taken <= h:
                result = min(result, middle)
                right = middle-1
            # else move left to middle +1.
            else:
                left = middle + 1                
        return result

