# Last updated: 12/6/2025, 5:52:21 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [2, 4] [1, 3]
# [1, 4] [2, 3]
# [1, 2] [4, 3]


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        arr = []
        node = head
        
        while node:
            arr.append(ListNode(node.val))
            node = node.next

        def helper(left, right):
            if left == right: return arr[left]
            mid = (left+right) // 2

            left = helper(left, mid)
            right = helper(mid+1, right)

            ans = ListNode(-1)
            curr = ans
            while left and right:
                if left.val <= right.val:
                    curr.next = ListNode(left.val)
                    curr = curr.next
                    left = left.next
                else:
                    curr.next = ListNode(right.val)
                    curr = curr.next
                    right = right.next
            
            if left:
                curr.next = left

            if right:
                curr.next = right
            
            return ans.next
        
        return helper(0, len(arr)-1)
