# Leetcode
# 61. Rotate List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return head
            
        current = tail = head

        length = 1
        while tail.next:
            length += 1
            tail = tail.next 
        
        # handle case where k is bigger than the length of the list.
        k = k % length
        # handle case where k is equal to the length of the list. 
        if k == 0: 
            return head 

        current = head
        for _ in range(length-k-1):
            current = current.next 
        new_head = current.next # Split the linked list after pointer has been moved k times. new_head has the 2nd part of the linked list and current has the 1st part of the linked list. 
        current.next = None # Set the EOL to the last element of the first list. 
        tail.next = head # Join the head of the first linked list to the end of the second linked list. 
        return new_head
