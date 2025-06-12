# Last updated: 12/6/2025, 5:53:43 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        head = ListNode(-101, head)
        node = head.next
        prev = head
        while node.next:
            if node.val == node.next.val:
                while node.next and node.next.val == node.val:
                    node = node.next
                node = node.next
                prev.next = node
                if not node: break
            else:
                prev = node
                node = node.next
        return head.next