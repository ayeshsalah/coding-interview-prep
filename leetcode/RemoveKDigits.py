# Leetcode
# 402. Remove K Digits
# https://www.youtube.com/watch?v=cFabMOnJaq0


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # maintain a monotonic stack, i. e., store only ascending values 
        monotonic_stack = []
        for char in num:
            # while we can remove digits and 
            # if last element in the stack in greater than current element, pop last element
            while k>0 and monotonic_stack and monotonic_stack[-1] > char:
                monotonic_stack.pop()
                k -= 1
            monotonic_stack.append(char)

        # if we have a positive k (the original string was monotonic, then remove the last k digits)
        # eg 124577
        monotonic_stack = monotonic_stack[:len(monotonic_stack)-k]
        # convert list to int then back to str to handle leading zeros
        return str(int("".join(monotonic_stack))) if monotonic_stack else "0"
