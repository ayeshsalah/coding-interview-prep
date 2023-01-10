# Leetcode
# 739. Daily Temperatures


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (index, value)

        # foor loop to iterate thru all the elements inthe array
        for index, value in enumerate(temperatures):
            # while loop to iterate thru the stack
            while stack and stack[-1][1]< value:
                stack_index, stack_value = stack.pop()
                result[stack_index] = index-stack_index
            stack.append((index, value))
        return result
