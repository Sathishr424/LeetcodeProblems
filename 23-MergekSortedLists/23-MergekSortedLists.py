# Last updated: 21/5/2025, 10:12:28 pm
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
        n = len(lists)
        if n == 0: return None
        elif n == 1: return lists[0]

        while len(lists) > 1:
            right = lists.pop()
            lists[-1] = self.mergeSort(lists[-1], right)
            index = random.randrange(0, len(lists))
            lists[index], lists[-1] = lists[-1], lists[index]
        
        return lists[0]
        
        