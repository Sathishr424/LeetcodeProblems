# Last updated: 12/6/2025, 5:52:13 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash = {}
        node = headA
        while node:
            hash[node] = 1
            node = node.next
        node = headB
        while node:
            if node in hash: return node
            node = node.next