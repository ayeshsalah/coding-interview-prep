# Leetcode
# 917. Reverse Only Letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # convert s to list of strings
        result = list(s)
        left = 0 
        right = len(s)-1

        while left<right:
            # if values at left and right are alpha, swap values and update counters
            if result[left].isalpha() and result[right].isalpha():
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1
            # if non alpha char is found, increment left or decrement right.
            if not result[left].isalpha():
                left += 1
            if not result[right].isalpha():
                right -= 1

        # convert list to string
        return "".join(result)
