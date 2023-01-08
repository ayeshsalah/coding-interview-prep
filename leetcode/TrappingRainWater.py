# Leetcode
# 42. Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        To find the trappable area at any given position, we need the minimum of the left or the right sides.
        Minimum[left or right] - current height = trappable area
        """
        max_left = height[0]
        max_right = height[len(height)-1]
        left = 0
        right = len(height)-1
        result = 0
        while left < right:
            # if max_left is smaller than max_right, then update max_left and 
            # add the difference of max_left and current height to result.
            # the order of max_left - current height is important 
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                # print(max_left - height[left])
                result += (max_left - height[left])
            # else max_left is larger than max_right, then update max_right and 
            # add the difference of max_right and current height to result.        
            # the order of max_right - current height is important    
            else:
                right -= 1
                max_right = max(max_right, height[right])
                # print(max_right - height[right])
                result += (max_right - height[right])
        return result
