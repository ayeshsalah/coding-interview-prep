# Leetcode
# 84. Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # store (index, height)
        max_area = 0

        for index, height in enumerate(heights):
            # Store the current index as start index
            start = index
            # check if the height in the stack is larger than current height,
            # if yes, pop the stack until the stack_height is smaller or stack is empty.
            while stack and stack[-1][1] > height:
                stack_index, stack_height = stack.pop()
                width = index-stack_index
                # calculate the area with the elements in the stack, compare with max_area and store greater value.
                max_area = max(max_area, stack_height*width)
                # update the start_index
                start = stack_index
            # adding start_index and current height to stack
            stack.append([start, height])

        # print(stack)
        # find max area of the values remaining in the stack
        while stack:
            stack_index, stack_height = stack.pop()
            # since the value(s) remained in the stack until the end of the heights array, 
            # the width will be len(heights) - stack_index
            width = len(heights)-stack_index
            max_area = max(max_area, stack_height*width)

        return max_area
