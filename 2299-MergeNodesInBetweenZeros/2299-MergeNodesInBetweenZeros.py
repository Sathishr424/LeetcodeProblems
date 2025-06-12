# Last updated: 12/6/2025, 5:38:31 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next
        left = head
        while node.next:
            if node.val == 0:
                left = left.next
                left.val = 0
            else:
                left.val += node.val
            node = node.next
        
        left.next = None
        return head