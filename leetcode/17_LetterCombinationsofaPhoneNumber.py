# Leetcode
# 17. Letter Combinations of a Phone Number
# https://www.youtube.com/watch?v=0snEunUacZY


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi" ,
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        if digits:
            self.back_track(0, "", result, digits, number_to_letters)
        return result

    def back_track(self, index, current_str, result, digits, number_to_letters):
        # base case
        # when length of current string is equal to the length of digits, add to result and return.
        if len(current_str) == len(digits):
            result.append(current_str)
            return 
        
        for c in number_to_letters[digits[index]]:
            self.back_track(index+1, current_str+c, result, digits, number_to_letters)
