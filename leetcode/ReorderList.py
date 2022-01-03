# Leetcode
# 143. Reorder List
# https://www.youtube.com/watch?v=S5bfdUTrKLM

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use slow and fast pointer to find the middle of the linked list
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse the 2nd half of the linked list 
        second = slow.next 
        slow.next = None # this will become the last element of the reordered list
        previous = None
        while second:
            temp = second.next # store reference to later elements in temp
            second.next = previous # update the .next with previous element. 
            previous = second # current element becomes the previous element for the next element in the LL
            second = temp # get back the reference to the remaining elements.
            
        # merge the 1st and 2nd(reversed) halves 
        second = previous # after list was reversed the previous will have the latest node i.e. the head of reversed list
        first = head
        # checking for second as it can be shorter than the first half.
        while second:
            temp1 = first.next #stores the 2nd element onwards of 1st list
            temp2 = second.next # stores the 2nd element onwards of 2nd list 
            
            first.next = second # inserting the element from 2nd list into the 1st list
            second.next = temp1 # making the connection to b/w the newly added element and the remainder of the 1st list
            
            second = temp2 # incrementing the pointer
            first = temp1 # incrementing the pointer
