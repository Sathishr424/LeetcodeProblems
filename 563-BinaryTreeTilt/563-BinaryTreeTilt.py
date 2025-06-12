# Last updated: 12/6/2025, 5:48:22 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def rec(node):
            nonlocal ret
            if node == None: return 0

            left = rec(node.left)
            right = rec(node.right)
            ret += abs(left-right)

            return left+right+node.val
        rec(root)
        return ret



