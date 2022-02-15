# Leetcode
# 797. All Paths From Source to target


# DFS solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # use a stack; start at element 0, continue down it's neighbours until the target(last element) is found. 
        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                result.append(path.copy())
                return

            next_nodes = graph[node]
            for next_node in next_nodes:
                dfs(next_node)
                path.pop()

        result = []
        path = []
        if not graph or len(graph) == 0:
            return result
        dfs(0)
        return result        


# BFS Solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # use a queue; start at element 0, add the possibe paths from 0. Pop 0 and continue with the first element in the queue. 
        paths = []
        if not graph or len(graph) == 0:
            return paths

        queue = deque()
        path = [0]
        queue.append(path)

        while queue:
            current_path = queue.popleft()
            node = current_path[-1]
            for next_node in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(next_node)

                if next_node == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)
        return paths
