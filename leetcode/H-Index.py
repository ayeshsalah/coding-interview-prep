# Leetcode
# 274. H-Index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        # print(citations)
        for i, citation in enumerate(citations):
            if i >= citation:
                return i 
        return len(citations)
