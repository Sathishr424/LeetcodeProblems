# Last updated: 12/6/2025, 5:55:47 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0)
        head = ret
        rem = 0
        while l1 and l2:
            val = l1.val+l2.val+rem
            rem = val//10
            val = val % 10
            ret.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            ret = ret.next
        while l1:
            val = l1.val+rem
            rem = val//10
            val = val % 10
            ret.next = ListNode(val)
            l1 = l1.next
            ret = ret.next
        while l2:
            val = l2.val+rem
            rem = val//10
            val = val % 10
            ret.next = ListNode(val)
            l2 = l2.next
            ret = ret.next
        if rem:
            ret.next = ListNode(rem)
        return head.next