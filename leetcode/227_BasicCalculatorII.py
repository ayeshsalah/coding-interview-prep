# Leetcode
# 227. Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/solutions/3227668/227-time-91-15-solution-with-step-by-step-explanation/


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = "+"
        current = 0
        for char in s+"+": # adding the + in the end because the last num in s will be added when an operator is found.
            if char.isdigit():
                current = current*10+int(char) # for consecutive digits. For eg. 98 => 9x10 + 8 = 98
            elif char in ["+", "-", "*", "/"]:
                if operator == "+":
                    stack.append(current)
                elif operator == "-":
                    stack.append(-current)
                elif operator == "*":
                    stack.append(stack.pop() * current)
                elif operator == "/":
                    stack.append(int(stack.pop()/current))
                operator = char
                current = 0
        return sum(stack)
