# Leetcode
# 21. Merge Two Sorted Lists


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # return_list to return the head of the merged sorted list
        # temp_list to iterate through both the lists
        # return_list.next will have reference to the newly created merged list
        return_list = temp = ListNode(0)
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        while list1 and list2:
            # set the value of temp list with smallest element from the 2 sorted lists
            # remove the element added to temp list from the main list
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            # add new element to temp list
            temp = temp.next
            
        # if lists of unequal lengths, add the remaining elements to temp list            
        temp.next = list1 or list2
            
        return return_list.next
