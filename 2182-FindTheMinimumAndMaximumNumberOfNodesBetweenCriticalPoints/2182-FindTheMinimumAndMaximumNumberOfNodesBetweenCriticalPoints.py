# Last updated: 12/6/2025, 5:38:58 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        last = -1
        prev = head.val
        node = head.next
        index = 1
        minD = float('inf')
        while node.next:
            index += 1
            if node.val < prev and node.val < node.next.val:
                if first == -1: first = index
                else: minD = min(minD, index - last)
                last = index
            elif node.val > prev and node.val > node.next.val:
                if first == -1: first = index
                else: minD = min(minD, index - last)
                last = index
            prev = node.val
            node = node.next
        if first == last: return [-1, -1]
        return [minD, last - first]