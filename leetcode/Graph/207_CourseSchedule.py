# Leetcode
# 207. Course Schedule
# https://www.youtube.com/watch?v=EgI5nU9etnU


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # testcase 
        # 5
        # [[0, 1], [0,2], [1,3], [1,4], [3,4]]

        # create adjacency list of courses and pre requisites
        # add every course id to adjacency list 
        adj_list = {i:[] for i in range(numCourses)}
        # populate pre-requisites for the given courses
        for course, pre_req in prerequisites:
            adj_list[course].append(pre_req)
        # print(adj_list)
        
        # run recursive dfs on all the node. Loop is needed incase of an unconnected graph. 
        for crs in range(numCourses):
            if not self.dfs(crs, adj_list, set()):
                return False
        return True
        
    def dfs(self, course, adj_list, visited):
        # check if the course is already visited, if yes return False. This os the check for cycle in the graph.
        if course in visited:
            return False
        # if the value in adj list is empty then no further prerequisites, return True
        if adj_list[course] == []:
            return True
        visited.add(course)
        pre_reqs = adj_list[course]
        for pr in pre_reqs:
            if not self.dfs(pr, adj_list, visited):
                return False
        # remove course from visited after is done visited. 
        visited.remove(course)
        # if no False was returned in the loop then all the pre requisites are met. We can change the value to empty list.
        adj_list[course] = []
        return True
