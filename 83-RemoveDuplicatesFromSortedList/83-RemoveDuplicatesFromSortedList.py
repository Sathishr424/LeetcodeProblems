# Last updated: 12/6/2025, 5:53:42 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head == None or head.next == None: return head
        ret = ListNode(200)
        tmp = ret
        while head:
            if tmp.val != head.val:
                tmp.next = ListNode(head.val)
                tmp = tmp.next
            head = head.next
        return ret.next