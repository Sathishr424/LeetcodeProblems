# Last updated: 12/6/2025, 5:51:50 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            if node.val == val:
                if prev: prev.next = node.next
                else: head = head.next
            else: prev = node
            node = node.next
        return head