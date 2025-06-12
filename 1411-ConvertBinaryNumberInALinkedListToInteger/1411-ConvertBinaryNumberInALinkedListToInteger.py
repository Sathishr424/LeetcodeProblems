# Last updated: 12/6/2025, 5:42:31 am
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        node = head
        length = 0
        ret = 0
        while node != None:
            length += 1
            node = node.next
        node = head
        cnt = 0
        while node != None:
            cnt += 1
            ret += int(node.val) * (2**(length-cnt))
            node = node.next
        return ret
        