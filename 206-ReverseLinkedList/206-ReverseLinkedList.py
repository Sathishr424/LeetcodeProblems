# Last updated: 12/6/2025, 5:51:46 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        node = head

        while node:
            curr = node.next
            node.next = prev
            prev = node
            node = curr
        return prev