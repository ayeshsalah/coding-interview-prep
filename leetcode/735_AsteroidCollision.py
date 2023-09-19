# Leetcode
# 735. Asteroid Collision


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                if stack[-1] + a < 0: # If right destroyed left, then there is a chance it could destroy more on the left, thus pop out left from stack, repeat check again
                    stack.pop()
                elif stack[-1] + a > 0: # If left destroyed right, then no more to destroy, break
                    break
                else:
                    stack.pop() # If both destroyed, no more to destroy, break
                    break
            else:
                stack.append(a)
        return stack
