# Leetcode
# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse() # reverse matrix
        matrix[:] = zip(*matrix) # transpose matrix and assign back to same object
