# Last updated: 12/6/2025, 5:47:23 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        ret = [None] * k
        for j in range(k):
            m = ceil(n/(k-j))
            newNode = ListNode(0)
            node = newNode
            n -= m
            for i in range(m):
                node.next = ListNode(head.val)
                node = node.next
                head = head.next
            ret[j] = newNode.next
        return ret