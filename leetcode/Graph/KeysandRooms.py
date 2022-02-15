# Leetcode
# 841. Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 1. set up a hashset with values up to len(rooms) - 1
        hashset = set(i for i in range(len(rooms)))
        # 3. initialize the visit function by going to the 0th room and checking out which keys you have
        self.visit(0, hashset, rooms)
        # 4. return not hashset, so True if it's empty, or False if the hashset has values in it
        return not hashset                                
                        
    # 2. set up a visit function that removes any seen index from an already seen room
    def visit(self, index, hashset, rooms):
        hashset.discard(index)
        for room in rooms[index]:
            if room in hashset:
                self.visit(room, hashset, rooms)
