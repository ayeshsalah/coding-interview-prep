# Leetcode
# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        result = 0
        for count in collections.Counter(s).values():
            # if count of char is even, add to result. 
            if count % 2 == 0:
                result += count
            # if count of char is odd, subtract 1 as Palindrome can only have 1 odd char in the middle.
            else:
                result += count-1
                odd = True
        # add the count of 1 odd char, when odd flag is true.
        if odd:
            result += 1
            
        return result
