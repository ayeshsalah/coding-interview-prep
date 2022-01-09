# Leetcode
# 997. Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # create list with equal trust for all residents
        trust_list = [0] * (n+1)
        # decrement the trust when a resident trusts someone
        # increment the trust when a resident is trusted 
        for a, b in trust:
            trust_list[a] -= 1
            trust_list[b] += 1
        print(trust_list)
        # since everyone trusts the judge except the judge, the judge's trsut will be n-1, if the judge exists.
        for i in range(1, n+1):
            if trust_list[i] == n-1:
                return i
        # if no resident has trust of n-1, there is no judge in the town. return -1. 
        return -1
