# Leetcode
# 155. Min Stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        potential_min = val
        if self.min:
            existing_min = self.min[-1]
            potential_min = min(potential_min, existing_min)
        self.min.append(potential_min)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.min:
            self.min.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.min:
            return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()