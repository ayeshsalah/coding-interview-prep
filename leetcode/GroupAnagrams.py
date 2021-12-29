# Leetcode
# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_hashmap = {}
        for item in strs:
            sorted_item = "".join(sorted(item))
            if sorted_item in sorted_hashmap:
                sorted_hashmap[sorted_item].append(item)
            else:
                sorted_hashmap[sorted_item] = [item]
        return sorted_hashmap.values()
