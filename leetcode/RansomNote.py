# Leetcode
# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_hashmap = {}
        magazine_hashmap = {}

        for i in ransomNote:
            ransom_hashmap[i] = ransom_hashmap.get(i, 0) + 1

        for i in magazine:
            if i in ransom_hashmap:
                magazine_hashmap[i] = magazine_hashmap.get(i, 0) + 1

        for key, value in ransom_hashmap.items():
            if key not in magazine_hashmap:
                return False
            elif magazine_hashmap[key] < value:
                return False
        return True

##########################################################################
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        mag_counter = collections.Counter(magazine)
        ransom_counter = collections.Counter(ransomNote)
        
        for alpha in ransom_counter:
            if ransom_counter.get(alpha, -1) > mag_counter.get(alpha, 0):
                return False
        return True
    
##########################################################################
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:  
        counter = collections.Counter(magazine)
        ransomNote = list(ransomNote)
        
        for alpha in list(ransomNote):
            ransomNote.remove(alpha)
            alpha_count = counter.get(alpha, -1)
            if alpha_count > 1:
                counter[alpha] = counter.get(alpha) - 1 
            elif alpha_count == 1:
                counter.pop(alpha)
            else:
                return False
            
        if not ransomNote:
            return True
        else:
            return False
            