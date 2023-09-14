# Leetcode
# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/1165015/Python3-Simple-recursive-and-iterative-solution-(with-figure-explanation)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = previous = ListNode()
        result.next = head
        current = head 

        while current and current.next: 
            if current.val == current.next.val:
                # when duplicates values are found iterate thru them all
                while current.next and current.val == current.next.val:
                    current = current.next
                # assign the current.next to current to remove the last duplicate element
                current = current.next
                # assign the previous.next to the head; thus skipping over all the duplicate elements                
                previous.next = current
            else:
                # when duplicates are not found increment both pointers
                current = current.next 
                previous = previous.next
        return result.next
