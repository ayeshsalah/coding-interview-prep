# Leetcode
# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        result_len = 0
        for i in range(len(s)):
            # odd palindromes
            left, right = i, i 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # check if length of current palindrome is greater then stored plaindrome 
                temp = s[left:right+1]
                if len(temp) > result_len:
                    result = temp
                    result_len = len(temp)
                left -= 1
                right += 1
                    
            # right palindromes
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # check if length of current palindrome is greater then stored plaindrome 
                temp = s[left:right+1]
                if len(temp) > result_len:
                    result = temp
                    result_len = len(temp)
                left -= 1
                right += 1
        return result
