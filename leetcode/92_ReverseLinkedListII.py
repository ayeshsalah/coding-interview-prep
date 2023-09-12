# Leetcode
# 92. Reverse Linked List II
# https://www.youtube.com/watch?v=RF_M9tX4Eag


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        left_prev = dummy
        current = head
        # reach node at left
        for i in range(left-1):
            left_prev = current
            current = current.next

        # reverse linked list
        previous = None
        for i in range(right-left+1):
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        # update the pointer at left and right
        left_prev.next.next = current # current is the node after "right"
        left_prev.next = previous  # previous is the right node

        return dummy.next
