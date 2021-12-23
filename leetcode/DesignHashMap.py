# Leetcode
# 706. Design HashMap
# Solution :  https://leetcode.com/problems/design-hashmap/discuss/795852/Python-solution-with-detailed-comments

class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.hash_map = [None] * self.capacity
        
    def get_index(self, key):
        """Hashing function"""
        return key % self.capacity    
        
    def put(self, key: int, value: int) -> None:

        index = self.get_index(key)
        # There are three(3) conditions to consider:
        # 1. If there is no key, value pair existing in the index, then create a new node to the index in hash table. 
        if self.hash_map[index] == None:
            self.hash_map[index] = Node(key,value)
        # If the key present in the index, then 
        else:
            # Initialize the current_node with the hash index. 
            current_node = self.hash_map[index]
            # Iterate through the loop while there is current_node
            while current_node:
                # 2. We check if the currrent_node has the same key as the new node, then we update the value and return.
                if current_node.key == key:
                    current_node.value = value
                    return
                # 3. If there is different keys with same hash index then we come out of the loop and
                if current_node.next:
                    current_node = current_node.next
                else:
                    break
            # add the new node to curr .next node.                        
            current_node.next = Node(key, value)
            

    def get(self, key: int) -> int:

        index = self.get_index(key)
        
        if self.hash_map[index] is None:
            return -1
        else:
            # current_node is the index of the hashtable
            current_node = self.hash_map[index]
            while current_node:
                # There are 2 conditions:
                # 1. if the key of the new node is same as the current_node then update the value
                if current_node.key == key:
                    return current_node.value
                # 2. If the key is not same then iterate through the list by incrementing the current node.
                else:
                    current_node = current_node.next
            return -1


    def remove(self, key: int) -> None:
        
        index = self.get_index(key)
        
        if self.hash_map[index]== None:
            return
        
        current_node = prev_node = self.hash_map[index]
        
        # To remove the key there are 3 conditions:
        # 1. if the current_node key matches with the key then update the hashtable index
        if current_node.key == key:
            self.hash_map[index] = current_node.next
        else:
            
            # Update the curr_ node to next
            current_node = current_node.next
            
            while current_node:
                
                # 2. If the curr node has the same key, update the pointer of prev to current.next. 
                # Break the condition and come out of the loop or else it will run infinitely. 
                if current_node.key == key:
                    prev_node.next = current_node.next
                    break
                
                # 3. If the key is not found, update the node in the bin.
                else:
                    prev_node = prev_node.next
                    current_node = current_node.next
                
        
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next=None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
