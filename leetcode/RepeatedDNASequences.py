# Leetcode
# 187. Repeated DNA Sequences
# The solution should be Rabin-Karp Algorithm with the Rabin fingerprinting hash. 
# Below answer is not Rabin-Kapr Algorithm. 

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set() # Set to handle cases where the same pattern is found twice. 
        seqs = set() # Stores all the sequences found by using rolling window of length 10.
        for i in range(len(s)-9): # len(s)-9 to compensate for range() not using the upper limit
            seq = s[i:i+10]
            if seq in seqs:
                result.add(seq)
            seqs.add(seq)
        return result
