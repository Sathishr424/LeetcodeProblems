# Last updated: 12/6/2025, 5:38:53 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head
        prev = None

        while right and right.next:
            prev = left
            left = left.next
            right = right.next.next
        
        if prev: prev.next = prev.next.next
        else: return None
        return head