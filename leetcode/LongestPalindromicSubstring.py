# Leetcode
# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0

        for i in range(len(s)):
            # odd 
            left, right = i, i 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # check if length of current palindrome is greater then stored plaindrome 
                if (right - left +1) > result_len:
                    result = s[left:right+1]
                    result_len = right - left +1
                left -= 1
                right += 1
                
            # even 
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # check if length of current palindrome is greater then stored plaindrome 
                if (right - left +1) > result_len:
                    result = s[left:right+1]
                    result_len = right - left +1
                left -= 1
                right += 1
        return result
