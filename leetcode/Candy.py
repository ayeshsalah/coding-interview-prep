# Leetcode
# 135. Candy 
# https://www.youtube.com/watch?v=h6_lIwZYHQw
# https://www.youtube.com/watch?v=2cDve2mTZvk 


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # find rewards in 2 passes, going forward and going backwards. 
        # compare neighbours and reward the higher ranked child.        
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        result = 0
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
        # print(left)
        for i in range(n-2, -1,-1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
        # print(right)
        for i in range(n):
            result += max(left[i], right[i])
        return result
