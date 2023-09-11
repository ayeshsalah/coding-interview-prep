# Leetcode
# 138. Copy List with Random Pointer
# https://www.youtube.com/watch?v=5Y2EiZST97Y

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None: None} # added None: None to handle end of list.

        # Create a new node with the same value as the current node and store it in the dictionary hash with the current node as the key.
        current = head
        while current:
            new_node = Node(current.val)
            hashmap[current] = new_node
            current = current.next 

        current = head
        while current: 
            new_node = hashmap[current] # Retrieve the copied node from the hash dictionary using current as the key and store it in the new_node variable.
            new_node.next = hashmap[current.next] # Set the next pointer of the new_node to the copied node obtained from the hash dictionary using current.next as the key.
            new_node.random = hashmap[current.random] # Set the random pointer of the new_node to the copied node obtained from the hash dictionary using current.random as the key.
            current = current.next 
        
        return hashmap[head]
