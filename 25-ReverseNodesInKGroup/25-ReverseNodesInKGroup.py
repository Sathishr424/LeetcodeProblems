# Last updated: 12/6/2025, 5:54:54 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        mid = k//2
        convert = False
        def helper(node, index):
            nonlocal left, convert
            if index >= k or node == None: return node
            elif index == k-1: convert = True
            ret = helper(node.next, index+1)
            if convert and index >= mid:
                tmp = node.val
                node.val = left.val
                left.val = tmp
                left = left.next
            return ret
        
        node = head
        cnt = 0
        left = None
        while node:
            left = node
            node = helper(node, 0)
            convert = False
        return head