# Leetcode
# 853. Car Fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted([[pos, s] for pos, s in zip(position, speed)])
        # print(sorted_pairs)
        stack = []
        for pos, spd in sorted_pairs[::-1]:
            # ETA is when the car will reach the destination
            eta = (target-pos)/spd 
            # Add ETA to stack when stack is empty 
            # OR
            # If the current ETA is greater than the head of the stack. i.e., there is no collision and new fleet is found. 
            if not stack or (stack and eta > stack[-1]): 
                stack.append(eta)
        return len(stack)
