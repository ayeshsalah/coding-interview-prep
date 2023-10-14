# Leetcode
# 148. Sort List
# https://www.youtube.com/watch?v=TGveA1oFhrc


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case; When not head, return None
        if not head:
            return 
        # another base case; When not head.next, return head. As only single node in list.
        if not head.next:
            return head

        # split list into 2
        # left becomes head of left list.
        left = head
        # find the middle and assign to middle.next to right
        middle = self.find_mid(head)
        right = middle.next 
        # Add None to break the list into 2.
        middle.next = None 


        # recusively call sortList to sort left and right lists
        left = self.sortList(left)
        right = self.sortList(right)
        # Return merged list
        return self.merge_list(left, right)

    def find_mid(self, head):
        slow = head
        fast = head
        # We check for fast.next and fast.next.next instead of fast and fast.next (like in problem #876) because when an even list is encountered, we get two elements in the middle, we want the left one. In problem #876, we wanted the right one.
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
        return slow

    def merge_list(self, left, right):
        # problem #88
        head = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        
        if left:
            dummy.next = left
        if right:
            dummy.next = right
        
        return head.next
