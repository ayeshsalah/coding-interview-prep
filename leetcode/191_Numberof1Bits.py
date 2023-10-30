# Leetcode
# 191. Number of 1 Bits


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0 
        while n:
            # modding by 2 will return 1 if the last digit is 1 or it will return zero
            # the sum of mod operations will give the number of zeros
            # >> is used to bitshift the chars to the right
            result += n % 2 
            n = n>>1
        return result
