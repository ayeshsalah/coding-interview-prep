# Leetcode
# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        # create dummy head
        dummy = ListNode()
        dummy.next = head
        
        current = nex = previous = dummy

        # find the length of the linked list
        length = 0
        while current:
            length += 1
            current = current.next

        # while the length of remaining nodes is greater than the size of the group i.e. k
        while length>k:
            current = previous.next # current will have the 1st node of the group; previous has the last node of the previous group
            nex = current.next # next will be the 2nd node of the group
            # reverse the nodes in the group, runs k-1 times
            for _ in range(k-1):
                current.next = nex.next
                nex.next = previous.next
                previous.next = nex
                nex = current.next
            previous = current # assign previous to the last node of the previous group
            length -= k # subtract size of the group
        return dummy.next
