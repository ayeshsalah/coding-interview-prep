# Leetcode
# 205. Isomorphic Strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_indices = []
        t_indices = []
        for c in s:
            s_indices.append(s.index(c))
        for c in t:
            t_indices.append(t.index(c))
        return s_indices == t_indices
