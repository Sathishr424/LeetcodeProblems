# Last updated: 12/6/2025, 5:53:20 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        first = True
        def helper(node):
            nonlocal prev, first
            if node == None: return True
            if not helper(node.left): return False
            if not first and node.val <= prev: return False
            else: first = False
            prev = node.val
            return helper(node.right)

        return helper(root)