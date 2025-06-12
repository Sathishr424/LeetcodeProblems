# Last updated: 12/6/2025, 5:38:46 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head

        prev = None
        node = head

        while fast and fast.next:
            # Find middle
            fast = fast.next.next
            # Reverse
            curr = node.next
            node.next = prev
            prev = node
            node = curr

        ret = 0
        while node:
            # print(prev.val, node.val)
            ret = max(ret, prev.val + node.val)
            prev = prev.next
            node = node.next
        
        return ret
        

        