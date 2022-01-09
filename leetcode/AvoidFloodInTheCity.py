#LeetCode 
#1488. Avoid Flood in The City

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        schedule_dict = collections.defaultdict(list)
        ret = [-1] * len(rains)
        to_empty = [] # index
        
        for day,lake in enumerate(rains):
            schedule_dict[lake].append(day)
        
        print(schedule_dict)
        
        for i in range(len(rains)):
            lake = rains[i]
            print("Lake : ",lake)
            if lake:
                if schedule_dict[lake] and schedule_dict[lake][0] < i:
                    print("Flood")
                    print(schedule_dict[lake])
                    return []
                if schedule_dict[lake] and len(schedule_dict[lake])>1:
                    print("Rain")
                    print(schedule_dict[lake])
                    print("Before heappush ", to_empty)
                    heapq.heappush(to_empty,schedule_dict[lake][1])
                    print("After heappush ", to_empty)
            else:
                if to_empty:
                    print("Lake can be dried")
                    print("Before heappop ", to_empty)
                    ret[i] = rains[heapq.heappop(to_empty)]
                    print("After heappop ", to_empty)
                    schedule_dict[ret[i]].pop(0)
                else:
                    print("No Lake to dry")
                    ret[i] = 1
        return ret
