# LeetCode
# 2. Add Two Numbers (without dummy head)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

######################################################################
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = temp_pointer = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = 0 # store current value of l1
            v2 = 0 # store current value of l2
            if l1:
                v1 = l1.val
                l1 = l1.next # l1 points to next node
            if l2:
                v2 = l2.val
                l2 = l2.next # l2 points to next node 
            current_sum = v1+v2+carry 
            val = current_sum % 10 # mod to get the value to be added to LL
            carry = current_sum // 10 # floor divison to find the carry value 
            temp_pointer.next = ListNode(val) # add sum value to LL
            temp_pointer = temp_pointer.next # increment the current node in the LL
        return result.next

######################################################################
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = None  # tracks head of result ListNode
        latest_node = None  # tracks the last added ListNode
        carry = 0  # stores the carry of summation
        l1_num = l2_num = 0
        while l1 or l2:  # while both ListNode are not None
            if l1:
                l1_num = l1.val
                l1 = l1.next  # next in ListNode l1
            if l2:
                l2_num = l2.val
                l2 = l2.next  # next in ListNode l2
            num_sum = l1_num + l2_num + carry
            digit = num_sum % 10  # new carry and sum's digit
            carry = num_sum // 10
            # carry, digit = divmod(num_sum, 10)
            new_node = ListNode(digit)
            if head:
                latest_node.next = new_node  # last node now points to new node
            else:
                head = new_node  # if first result ListNode
            latest_node = new_node  # new node is now last node
            l1_num = l2_num = 0
        if carry != 0:  # if there is a carry at the end
            carry_node = ListNode(carry)  # add a new ListNode
            latest_node.next = carry_node
            latest_node = carry_node
        return head
