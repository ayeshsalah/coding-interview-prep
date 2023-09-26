# Leetcode
# 316. Remove Duplicate Letters


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hashmap = {} # key: alphabet, value: max index of alphabet
        for i, a in enumerate(s):
            hashmap[a] = i

        stack = [] # to store the result
        seen = set() # used to check if alphabet is in stack
        for i, a in enumerate(s):
            # check if alphabet is in stack
            if a in seen:
                continue
            # if elements in stack AND
            # top element of stack is greater than the current element AND
            # top element of stack's max index greater than current index
            while stack and stack[-1]>a and hashmap[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(a)
            seen.add(a)
        return "".join(stack)
