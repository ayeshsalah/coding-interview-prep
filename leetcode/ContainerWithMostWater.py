# Leetcode
# 11. Container With Most Water
# https://www.youtube.com/watch?v=UuiTKBwPgAo


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        area = 0
        while left<right:
            curr_width = right-left
            curr_height = min(height[left], height[right])
            area = max(curr_height*curr_width, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1 
        return area
