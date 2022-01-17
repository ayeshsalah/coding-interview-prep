# Leetcode
# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # reverse number and compare if the number is the same 
        # https://www.geeksforgeeks.org/write-a-program-to-reverse-digits-of-a-number/
        num = x
        reverse = 0 
        while num > 0: # negative numbers won't be a palindrome. 
            reverse = num %10 + reverse * 10
            num = num//10
        return x == reverse
