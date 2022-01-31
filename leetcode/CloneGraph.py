# Leetcode
# 133. Clone Graph
# https://www.youtube.com/watch?v=mQeF6bN8hMk

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            old_to_new = {}
            return self.clone(node, old_to_new)
        
    def clone(self, node, old_to_new):
        # if node in hashmap
        if node in old_to_new:
            return old_to_new[node]
        # when node not in hashmap
        copy = Node(node.val)
        # add to hashmap
        old_to_new[node] = copy
        # run clone for all the neighbors
        for neigh in node.neighbors:
            # append result of neighbour's clone to copy's neighbors
            neigh_clone = self.clone(neigh, old_to_new)
            copy.neighbors.append(neigh_clone)
        return copy
