# Last updated: 12/6/2025, 5:55:04 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0)
        head = ret

        while l1 and l2:
            if l1.val < l2.val:
                ret.next = ListNode(l1.val)
                l1 = l1.next
            else:
                ret.next = ListNode(l2.val)
                l2 = l2.next
            ret = ret.next
        while l1:
            ret.next = ListNode(l1.val)
            l1 = l1.next
            ret = ret.next

        while l2:
            ret.next = ListNode(l2.val)
            l2 = l2.next
            ret = ret.next
        
        return head.next