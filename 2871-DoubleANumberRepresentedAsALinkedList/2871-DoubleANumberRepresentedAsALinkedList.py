# Last updated: 12/6/2025, 5:36:43 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(node):
            if node == None: return 0
            tmp = rec(node.next)
            val = node.val * 2
            if tmp + val >= 10:
                node.val = (tmp+val) - 10
                return (tmp+val) // 10
            else:
                node.val = tmp + val
            return 0
        ans = rec(head)
        if ans > 0:
            node = ListNode(ans)
            node.next = head
            return node
        return head
        