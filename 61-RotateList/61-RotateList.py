# Last updated: 12/6/2025, 5:54:11 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0 or head.next == None: return head
        n = 0
        node = head
        last = None
        while node:
            last = node
            node = node.next
            n += 1
        
        k = n - (k % n)
        if k == n: return head

        prev_head = head
        node = head
        i = 0

        while node and i+1 < k:
            i += 1
            node = node.next
        ret = node.next
        node.next = None
        last.next = head
        return ret