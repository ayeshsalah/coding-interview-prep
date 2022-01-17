# Leetcode
# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # brute force, O(3n) time and O(1) space
        # cleaned = "".join([c for c in s.lower() if c.isalnum()])
        # return cleaned == cleaned[::-1]
        
        # 2 pointer, O(n) time and O(1) space
        left = 0
        right = len(s)-1
        while left <= right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1
            if s[left].lower() == s[right].lower():
                left += 1
                right -=1
            else:
                return False
        return True
