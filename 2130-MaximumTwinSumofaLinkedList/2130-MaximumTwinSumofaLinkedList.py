# Last updated: 16/8/2025, 6:50:30 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_val = 0
        def rec(slow, fast):
            nonlocal max_val
            if fast.next == None:
                max_val = max(max_val, slow.val + slow.next.val)
                return slow.next.next
            node = rec(slow.next, fast.next.next)
            max_val = max(max_val, node.val + slow.val)
            return node.next

        rec(head, head.next)
        return max_val