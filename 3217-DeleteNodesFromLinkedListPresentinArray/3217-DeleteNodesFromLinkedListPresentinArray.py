# Last updated: 1/11/2025, 12:40:08 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        def rec(node):
            if node == None: return None

            if node.val in nums:
                return rec(node.next)
            node.next = rec(node.next)
            return node
        
        return rec(head)