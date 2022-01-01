# Leetcode
# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_pointer = headA
        b_pointer = headB
        
        #  concatenate the lists in opposite orders, A+B and B+A. 
        # This way, the ends of the two original lists will align on the second half of each merged list.
        while a_pointer != b_pointer:
            a_pointer = headB if not a_pointer else a_pointer.next
            b_pointer = headA if not b_pointer else b_pointer.next
        return a_pointer
