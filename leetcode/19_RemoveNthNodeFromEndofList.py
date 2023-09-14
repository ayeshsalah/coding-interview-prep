# Leetcode
# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1164537/Short-and-Simple-One-Pass-Solution-w-Explanation-or-Beats-100-or-No-dummy-node-required!

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer approach
        slow = fast = head
        # move fast pointer by n places
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        # iterate thru until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next 
        # 'slow' is at (n+1)th node from end.
        # delete nth node from end by assign the n+1's next to nth's next.
        slow.next = slow.next.next
        return head
