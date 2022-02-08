# Leetcode
# 1202. Smallest String With Swaps
# https://www.youtube.com/watch?v=1Ga44vFth8k

#TODO add explanation

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        disjoint_set = UnionFind(len(s))
        
        for x, y in pairs:
            disjoint_set.union(x, y)
            
        
        dic = defaultdict(list)
        
        # print(disjoint_set.root)
        
        # 0: [0, 3]
        # 1: [1, 2]
        for index, element in enumerate(disjoint_set.root):
            dic[disjoint_set.find(element)].append(index)
            
        # print(dic)
        
        result = list(s)
        
        for key in dic.keys():
            index_list = dic[key]
            char_list = [s[i] for i in index_list]
            char_list.sort()
            
            for idx, char in zip(index_list, char_list):
                result[idx] = char
                
        return "".join(result)
