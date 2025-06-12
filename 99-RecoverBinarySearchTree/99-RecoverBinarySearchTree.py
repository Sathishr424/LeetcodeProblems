# Last updated: 12/6/2025, 5:53:19 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = None
        second = None
        prev = None

        def rec(node):
            nonlocal first, second, prev
            if node == None: return
            rec(node.left)
            if prev and prev.val > node.val:
                if not first: 
                    first = prev
                    second = node
                else: 
                    second = node
                    return
            prev = node
            rec(node.right)
        rec(root)

        first.val, second.val = second.val, first.val
            