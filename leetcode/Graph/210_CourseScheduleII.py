# Leetcode
# 210. Course Schedule II
# https://www.youtube.com/watch?v=Akt3glAwyfY


class Solution:
    # Topological Sort 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list
        adj_list = {i:[] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            adj_list[course].append(pre_req)
        result = []
        # course can have 3 possible states 
        # visited -> Has been added to result
        # current -> Not added to result but added to current
        # unvisited -> Not added to result or current        
        visited = set()
        current = set()

        for course in range(numCourses):
            if not self.dfs(course, adj_list, visited, current, result):
                return []
        return result
    
    def dfs(self, item, adj_list, visited, current, result):
        # if item in current, it is being visited twice.
        if item in current:
            return False
        # if item in visited, we have already visited item, no need to visit again. We can continue DFS.
        if item in visited:
            return True
        # add item to current
        current.add(item)
        # run dfs on all pre requisties of item
        pre_reqs = adj_list[item]
        for pre_req in pre_reqs:
            if not self.dfs(pre_req, adj_list, visited, current, result):
                return False
        # remove from current and add to visited and result.
        current.remove(item)
        visited.add(item)
        result.append(item)
        return True
