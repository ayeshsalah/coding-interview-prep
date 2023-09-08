# Leetcode
# 71. Simplify Path


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        split_path = path.split("/")
        for item in split_path:
            if stack and item == "..":
                stack.pop()
            elif item not in [".", "..", ""]:
                stack.append(item)
        return "/" + "/".join(stack)
