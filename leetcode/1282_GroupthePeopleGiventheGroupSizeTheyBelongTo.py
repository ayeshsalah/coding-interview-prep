# Leetcode
# 1282. Group the People Given the Group Size They Belong To


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = {} # key: group size, value: list of indices. Eg. {3:[0, 1, 2]}
        result = []

        for i, size in enumerate(groupSizes):
            # check if group size already exists in hashmap, append index if it exits, exists add a new key. 
            if size in hashmap:
                hashmap[size].append(i)
            else:
                hashmap[size] = [i]
            
            # When the list reaches the desired group size, apeend the list to result and reset the array.
            if len(hashmap[size]) == size:
                result.append(hashmap[size])
                hashmap[size] = []
        return result
