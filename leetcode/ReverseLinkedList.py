#LeetCode 
#206. Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            temp = current.next # store reference to later elements in temp
            current.next = previous # update the .next with previous element. first value will be None as the tail of LL is None.
            previous = current # current element becomes the previous element for the next element in the LL
            current = temp # get back the reference to the remaining elements. 
        return previous


################################################
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous, current = None, head
        while current:
            current.next, previous, current =  previous, current, current.next
        return previous
