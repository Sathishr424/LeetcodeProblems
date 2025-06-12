# Last updated: 12/6/2025, 5:53:39 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head = ListNode(-201, head)
        node = head.next
        prev = head
        arr = []
        while node:
            if node.val >= x:
                arr.append(node.val)
                prev.next = node.next
            else:
                prev = node
            node = node.next
        for val in arr:
            prev.next = ListNode(val)
            prev = prev.next
        return head.next
