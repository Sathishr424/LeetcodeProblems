# Last updated: 12/6/2025, 5:52:45 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = -1001
        def helper(node):
            nonlocal ret
            if node == None: return 0
            left = helper(node.left)
            right = helper(node.right)
            val = max(node.val+left, node.val+right, node.val)
            ret = max(ret, node.val+left+right, val)
            return val
        helper(root)
        return ret