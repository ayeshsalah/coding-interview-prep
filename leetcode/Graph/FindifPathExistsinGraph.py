# Leetcode
# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/discuss/1511658/Simple-Solution-DFS


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # convert edges to dict 
        # input : n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
        # {0: [1, 2], 1: [0, 2], 2: [1, 0]}
        graph_dict = {}
        for edge in edges:
            v1, v2 = edge
            if v1 in graph_dict.keys():
                graph_dict[v1].append(v2)
            else:
                graph_dict[v1] = [v2]
            if v2 in graph_dict.keys():
                graph_dict[v2].append(v1)
            else:
                graph_dict[v2] = [v1]
        return self.is_path(graph_dict, source, destination, set())
        
    def is_path(self, graph, current, target, visited):
        if current == target:
            return True
        if current in visited:
            return False
        visited.add(current)
        for neighbour in graph[current]:
            if self.is_path(graph, neighbour, target, visited) == True:
                return True
        return False
