# Last updated: 1/11/2025, 12:42:57 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        node = head
        while node and node.val in nums:
            node = node.next
        head = node
        while node.next:
            if node.next.val in nums:
                node.next = node.next.next
                continue
            node = node.next
        
        return head
