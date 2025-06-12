# Last updated: 12/6/2025, 5:51:15 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        def rec(node):
            nonlocal left
            if node == None: return True
            if not rec(node.next) or node.val != left.val: return False
            left = left.next
            return True
        return rec(head)