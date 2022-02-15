# Leetcode
# 210. Course Schedule II
# https://www.youtube.com/watch?v=Akt3glAwyfY

class Solution:
    # Topological Sort 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            adj_list[course].append(pre_req)       
        # print(adj_list)
        # course can have 3 possible states 
        # visited -> Has been added to result
        # visiting -> Not added to result but added to current
        # unvisited -> Not added to result or current
        result = []
        visiting = set()
        current = set() # used to detect cycle 
        
    
        def dfs(item):
            # if item in current, it is being visited twice.
            if item in current:
                return False
            # if item in visiting, we have already visited item, no need to visit again. We can continue DFS.
            if item in visiting:
                return True
            # add item to current
            current.add(item)
            # run DFS on all the prerequisites of the item
            for pre_req in adj_list[item]:
                if not dfs(pre_req):
                    return False
            current.remove(item)
            visiting.add(item)
            result.append(item)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result    
