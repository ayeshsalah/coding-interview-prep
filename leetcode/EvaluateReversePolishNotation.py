# Leetcode
# 150. Evaluate Reverse Polish Notation


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            elif item == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif item == "*":
                stack.append(stack.pop() * stack.pop())         
            elif item == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(item))
        return stack[0]
