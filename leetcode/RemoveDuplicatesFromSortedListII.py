# Leetcode
# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/1165015/Python3-Simple-recursive-and-iterative-solution-(with-figure-explanation)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = previous = ListNode()
        result.next = head
        
        while head and head.next:
            if head.val == head.next.val:
                # when duplicates values are found iterate thru them all
                while head.next and head.val == head.next.val:
                    head = head.next
                # assign the head.next to head to remove the last duplicate element
                head = head.next
                # assign the previous.next to the head; thus skipping over all the duplicate elements
                previous.next = head
            else:
                # when duplicates are not found increment both pointers
                head = head.next
                previous = previous.next
        return result.next
