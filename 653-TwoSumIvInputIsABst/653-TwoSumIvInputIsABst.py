# Last updated: 12/6/2025, 5:47:52 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash = {}
        def rec(node):
            if node == None: return False
            if k-node.val in hash: return True
            hash[node.val] = 1
            if rec(node.left): return True
            if rec(node.right): return True
            return False
        return rec(root)