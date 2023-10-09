# Leetcode
# 22. Generate Parentheses


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # use stack to keep track of the parentheses added. 
        # use recursion to find all the combinations

        stack = []
        result = []
        self.back_track(n, 0, 0, stack, result)
        return result        

    def back_track(self, n, open_counter, close_counter, stack, result):
        #base case, when open and close counter are equal to n.
        if n == open_counter == close_counter:
            result.append("".join(stack))
            return
        # when open counter is less than n
        if open_counter < n:
            stack.append("(")
            self.back_track(n, open_counter+1, close_counter, stack, result)
            stack.pop()
        # when close counter is less then open counter
        if close_counter < open_counter:
            stack.append(")")
            self.back_track(n, open_counter, close_counter+1, stack, result)
            stack.pop()
