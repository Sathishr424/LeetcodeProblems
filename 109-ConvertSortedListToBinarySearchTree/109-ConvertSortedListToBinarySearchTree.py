# Last updated: 12/6/2025, 5:53:06 am
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node = head
        arr = []
        while node:
            arr.append(node)
            node = node.next

        def sub(left, right):
            if left > right: return None
            mid = (left+right)//2

            return TreeNode(arr[mid].val, sub(left, mid-1), sub(mid+1, right))
        
        return sub(0, len(arr)-1)