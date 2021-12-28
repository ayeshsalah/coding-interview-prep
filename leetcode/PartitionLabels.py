# Leetcode
# 763. Partition Labels
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find the last occurance of every alphabet in s and store that index. 
        last_index = {}
        for index, alpha in enumerate(s):
            last_index[alpha] = index
         
        result = []            
        max_last_index = 0
        count = 0
        # find the max between max_last_index and last_index of current alpha. 
        # if current alpha's last index equals the max_last index
        # then add the current index to result and reset max_last_index to 0. 
        # finding the max for every iteration ensures only the correct index is added into result
        for index, alpha in enumerate(s):
            max_last_index = max(max_last_index, last_index[alpha])
            count += 1
            if index == max_last_index:
                result.append(count)
                count = 0
        return result
