# Last updated: 12/6/2025, 5:44:52 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        def rec(node):
            return node == None or (node.val == val and rec(node.left) and rec(node.right))
        
        return rec(root.left) and rec(root.right)