# Last updated: 21/5/2025, 10:26:14 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_lists = []
        for l in lists:
            if l: new_lists.append(l)
        
        new_lists.sort(key=lambda x: x.val)
        lists = new_lists
        if len(lists) == 0: return None

        def mergeSort(left, right):
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
        
        while len(lists) > 1:
            new_lists = []

            while len(lists) > 1:
                new_lists.append(mergeSort(lists.pop(), lists.pop()))
            if lists:
                new_lists.append(lists[0])
            
            lists = new_lists
        
        return lists[0]