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

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        return self.dfs_clone(node, hashmap)

    def dfs_clone(self, node, hashmap):
        if not node:
            return None
        # check if node already exists in the hashmap, if so return the node.
        if node in hashmap:
            return hashmap[node]
        # if valid node and not in hashmap, create a copy and add copy to hashmap.
        # create copies of the neighbors of the node, add to hashmap and append to copy_node's neighbors. 
        # return copy_node.
        copy_node = Node(node.val)
        hashmap[node] = copy_node
        for neighbor in node.neighbors:
            copy_neighbor = self.dfs_clone(neighbor, hashmap)
            copy_node.neighbors.append(copy_neighbor)
        return copy_node
