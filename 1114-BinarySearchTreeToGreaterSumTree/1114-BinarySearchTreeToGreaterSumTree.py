# Last updated: 12/6/2025, 5:44:04 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def rec(node, sum=0):
            if node == None: return sum
            node.val += rec(node.right, sum)
            return rec(node.left, node.val)
        rec(root)
        return root