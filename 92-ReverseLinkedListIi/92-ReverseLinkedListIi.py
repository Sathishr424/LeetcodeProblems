# Last updated: 12/6/2025, 5:53:29 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        n = right-left
        mid = n // 2
        for i in range(1, left): node = node.next
        def rec(node, index):
            nonlocal left
            if index > n: return
            rec(node.next, index+1)
            if index > mid:
                tmp = node.val
                node.val = left.val
                left.val = tmp
                left = left.next
        left = node
        rec(node, 0)
        return head