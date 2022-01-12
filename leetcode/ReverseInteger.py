#LeetCode
#7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        # String approach 
        reverse_num = int(str(abs(x))[::-1])
        if reverse_num.bit_length() >= 32:
            return 0 
        if x < 0:
            reverse_num = -reverse_num
        return reverse_num
    
    def reverse(self, x: int) -> int:
        # math approach
        num = x
        negative_flag = 1
        
        if num < 0:
            num = -num
            negative_flag = -1
            
        reverse = 0
        
        while num:
            reverse = num%10 + reverse*10
            num = num//10
            
        # check for 32-bit int overflow.
        if reverse > pow(2, 31):
            return 0
        return reverse * negative_flag
