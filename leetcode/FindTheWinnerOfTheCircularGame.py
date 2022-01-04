# Leetcode
# 1823. Find the Winner of the Circular Game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # create a double ended queue object 
        # rotate the queue to the left
        # negative number rotates the queue to the left 
        # pop last element
        elements = collections.deque([x for x in range(1, n+1)])
        # print(elements)
        while len(elements) > 1:
            elements.rotate(-k)
            # print(elements)
            elements.pop()
        return elements.pop()
