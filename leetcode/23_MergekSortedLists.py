# Leetcode
# 23. Merge k Sorted Lists
# https://www.youtube.com/watch?v=q5a5OiGbT6Q (divide and conquer solution)
# https://leetcode.com/problems/merge-k-sorted-lists/discuss/1032502/Python-Simple-Heap-Solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while(len(lists)>1):
            merged_lists = []
            # using the helper function to merge 2 lists at a time
            # store the merged lists in an array
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.merge_two_lists(list1, list2))
            # replace the original lists array with the merged lists array, until only 1 list remains.
            lists = merged_lists
        # return the last list in the array.
        return lists[0]

    def merge_two_lists(self, list1, list2):
        # merge 2 sorted linked lists
        # leetcode 21
        if not list1:
            return list2
        if not list2:
            return list1 
        return_list = temp_list = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                temp_list.next = list1
                list1 = list1.next
            else:
                temp_list.next = list2
                list2 = list2.next
            temp_list = temp_list.next
        temp_list.next = list1 or list2
        
        return return_list.next
