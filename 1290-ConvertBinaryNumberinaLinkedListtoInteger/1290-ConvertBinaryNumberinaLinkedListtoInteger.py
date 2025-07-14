# Last updated: 14/7/2025, 11:51:34 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def rec(node):
            if node == None: return 0, 0
            val, power = rec(node.next)
            if node.val == 1:
                val += 1 << power
            return val, power + 1
        
        return rec(head)[0]