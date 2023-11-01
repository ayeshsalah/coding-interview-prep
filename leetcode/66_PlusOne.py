# Leetcode
# 66. Plus One


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # check if last digit is 9
        if digits[-1] == 9:
            # if last digits is 9 and length of digits is 1, return list with [1, 0]
            if len(digits) == 1:
                return [1, 0]
            # else recursively call the function and append [0]
            else:
                return self.plusOne(digits[:-1]) + [0]
        # if lasy digit is not 9, increment it by 1
        else:
            digits[-1] += 1
            return digits
