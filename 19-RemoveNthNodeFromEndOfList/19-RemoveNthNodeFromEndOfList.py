# Last updated: 12/6/2025, 5:55:06 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None: return None
        cnt = 0
        def rec(node):
            nonlocal cnt
            if node == None: return 0
            index = rec(node.next)
            cnt += 1
            if index == n:
                node.next = node.next.next
                return 31
            return index+1
        index = rec(head)
        if index == cnt: return head.next
        return head