# Leetcode
# 142. Linked List Cycle II

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        # first check if cycle exists; Break if cycle exists, else return None.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        # whencycle exsits
        # increment the slow pointer and head until they are equal. This node is the start of the cycle.
        while head and slow:
            if head == slow:
                return head
            else:
                head = head.next 
                slow = slow.next
        # while head!=slow:
        #     print(slow.val)
        #     print(head.val)
        #     slow = slow.next
        #     head = head.next
        # return head
