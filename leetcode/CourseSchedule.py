# Leetcode
# 207. Course Schedule
# https://www.youtube.com/watch?v=EgI5nU9etnU


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # testcase 
        # 5
        # [[0, 1], [0,2], [1,3], [1,4], [3,4]]

        # create adjacency list of cources and pre requisites
        adj_list = {i:[] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            adj_list[course].append(pre_req)
            
        # print(adj_list)
        # run recursive dfs on all the node. Loop is needed incase of an unconnected graph. 
        for crs in range(numCourses):
            if not self.dfs(crs, adj_list, set()):
                return False
        return True
        
    def dfs(self, item, adj_list, visiting):
        # check if the item is already visited, if yes return False
        if item in visiting:
            return False
        # if the value in adj list is empty then no further prerequisites, return True
        if adj_list[item] == []:
            return True
        visiting.add(item)
        pre_reqs = adj_list[item]
        for pr in pre_reqs:
            if not self.dfs(pr, adj_list, visiting):
                return False
        # remove item from visiting after is done visiting. 
        visiting.remove(item)
        # if no False was returned in the loop then all the pre requisites are met. We can change the value to empty list.
        adj_list[item] = []
        return True
