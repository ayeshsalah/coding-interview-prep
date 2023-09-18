# Leetcode
# 146. LRU Cache
# https://www.youtube.com/watch?v=7ABFKPK2hD4

class Node:
    """Class for Doubly Linked List"""
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Left is the Least Recently Used
        self.left = Node(0, 0)
        # Right is the Most Recently Used
        self.right = Node(0, 0)
        # Linking the 2 nodes, both ways.
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        """Removes node from LL. node wil be the middle node, so find prev, next and update them"""
        prev = node.prev
        nxt = node.next
        prev.next = nxt 
        nxt.prev = prev

    def _insert(self, node):
        """ Insert node at the 1 place before the right most pointer """
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt 
        node.prev = prev
        
    def get(self, key: int) -> int:
        """Update the node to most recently used and retuen the value"""
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        """Add to cache, if item exits, update value"""
        if key in self.cache:
            self._remove(self.cache[key])
        # add to cache
        self.cache[key] = Node(key, value)
        # add to linked list
        self._insert(self.cache[key])

        # check if cache is at capacity
        # if yes, remove from cache and linked list
        if len(self.cache) > self.capacity:
            lru = self.left.next # left.next always hold the LRU
            self.cache.pop(lru.key)
            self._remove(lru)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)