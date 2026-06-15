# Last updated: 6/15/2026, 12:10:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        slow = head
9        fast = head
10        prev_slow = head
11
12        while fast and fast.next:
13            prev_slow = slow
14            slow = slow.next
15            fast = fast.next.next
16        
17        if prev_slow and prev_slow.next:
18            prev_slow.next = prev_slow.next.next
19        else:
20            return None
21        
22        return head
23
24
25
26