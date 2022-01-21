# Leetcode
# 647. Palindromic Substrings
# Similar to Leetcode 5

class Solution:
    def countSubstrings(self, s: str) -> int:
        # iterate thru all the elements considering the current element as the middle of the palindrome
        # change index for odd length and even length palindrome
        odd, even = 0, 0
        for i in range(len(s)):
            # odd palindromes
            odd += self.checkPalindrome(s, i, i)
            # right palindrome
            even += self.checkPalindrome(s, i, i+1)
        return odd+even
        
    def checkPalindrome(self, string, left, right):
        count = 0
        # check if left and right are within bounds and chars are left and right index are same
        while left>=0 and right<len(string) and string[left]==string[right]:
            count += 1
            left -=1 # subtract 1 to move left fromthe middle
            right +=1 # add one to move right from the middle
        return count
