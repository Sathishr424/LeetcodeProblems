# Last updated: 12/6/2025, 5:52:38 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def helper(node, tot):
            nonlocal ret
            if node == None: return
            elif node.left == None and node.right == None:
                ret += tot * 10 + node.val
            else:
                val = tot * 10 + node.val
                helper(node.left, val)
                helper(node.right, val)
        helper(root, 0)
        return ret