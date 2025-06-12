# Last updated: 12/6/2025, 5:40:33 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        i = 1
        while i < a:
            node = node.next
            i += 1
        tmp = node
        while i <= b:
            node = node.next
            i += 1
        tmp.next = list2
        node2 = list2
        while node2.next:
            node2 = node2.next
        node2.next = node.next
        return list1
