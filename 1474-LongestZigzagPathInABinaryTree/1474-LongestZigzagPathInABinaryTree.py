# Last updated: 12/6/2025, 5:42:07 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def rec(node, prev, cnt):
            nonlocal res
            res = max(res, cnt)
            if node == None: return

            rec(node.left, 'L', cnt + 1 if prev == 'R' else 0)
            rec(node.right, 'R', cnt + 1 if prev == 'L' else 0)
        
        rec(root, '', 0)
        return res
