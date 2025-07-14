# Last updated: 14/7/2025, 5:29:01 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        val = 0
        while head:
            val *= 2
            if head.val == 1:
                val += 1
            head = head.next
        
        return val