# Leetcode
# 744. Find Smallest Letter Greater Than Target


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # if the number is out of bound
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        # when target is within bounds
        # Apply the binary search with only one change 
        # when updating the bottom boundary check if the target is greater than or equal to the mid value 
        # (In binary search we only check if it is greater than)
        # since we are asked to return the value above the target value we want to keep track of the value one step above the low value
        # when the low > high, we return the letters[low]
        low = 0
        high = len(letters)-1
        while low <= high:
            mid = (high+low)//2
            if  target >= letters[mid]: # in binary search this would be only greater than
                low = mid+1
            if target < letters[mid]:
                high = mid-1
                
        return letters[low]
