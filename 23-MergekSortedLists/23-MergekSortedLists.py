# Last updated: 21/5/2025, 10:01:45 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self, left, right):
        new_list = ListNode()
        head = new_list

        while left and right:
            if left.val < right.val:
                new_list.next = ListNode(left.val)
                left = left.next
            else:
                new_list.next = ListNode(right.val)
                right = right.next
            new_list = new_list.next
        
        if left: new_list.next = left
        else: new_list.next = right
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        elif len(lists) == 1: return lists[0]

        n = len(lists)
        if n % 2: lists.append(None)
        
        new_lists = []
        for i in range(0, n, 2):
            new_lists.append(self.mergeSort(lists[i], lists[i+1]))
        
        return self.mergeKLists(new_lists)