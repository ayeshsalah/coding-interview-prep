# Leetcode
# 957. Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/discuss/411559/python-general-solution-beats-83.26-w-commentary
    
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        day = 0 
        hashmap = {}
        daily_states = []
        cells = tuple(cells)
        
        while cells not in hashmap:
            if day == n:
                return cells
            daily_states.append(list(cells))
            hashmap[cells] = day            
            day += 1
            new_cells = [0] * len(cells)
            for i in range(1, len(cells)-1):
                # 2 same integers would get the result of 0 (x^x = 0)
                new_cells[i] = 1 if (cells[i-1] ^ cells[i+1] == 0) else 0
            
            cells = tuple(new_cells)
          
        # for row in daily_states:
        #     print(row)
            
        loop_start = hashmap[cells]
        loop_length = day - loop_start 
        result = loop_start+(n-loop_start)%loop_length
        
        # print("loop start:",loop_start)     
        # print("loop length:",loop_length)
        # print("result:",result)
        
        return daily_states[result]
