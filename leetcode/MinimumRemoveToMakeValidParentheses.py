# Leetcode
# 1249. Minimum Remove to Make Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
                 
        # convert string to list 
        s_list = list(s)    
        stack = []
                 
        for index, alphabet in enumerate(s_list):
            if alphabet  == "(":
                # store index of opening parenthesis
                stack.append(index)
            elif alphabet == ")":
                if stack:
                    # if closing parenthesis is found and stack has value, pop stack.
                    stack.pop()
                else:
                    # if stack is empty and closing parenthesis is found, replace with empty string.
                    s_list[index] = ""
                    
        # if stack has values, must be opening parenthesis, replace with empty string.              
        while stack:
            s_list[stack.pop()] = ""
        
        # convert back to str and return
        return "".join(s_list)
