# Leetcode
# 86. Partition List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = small_head = ListNode()
        large = large_head = ListNode()

        while head:
            # if val is greater or equal to x, add to large.
            if head.val >= x:
                large.next = ListNode(head.val)
                large = large.next
            # else add to small.
            else:
                small.next = ListNode(head.val)
                small = small.next
            head = head.next
        # assign the last node of small to the head of large, to merge the 2 lists. 
        small.next = large_head.next
        return small_head.next
