# Last updated: 12/6/2025, 5:48:35 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = -float('inf')
        ans = float('inf')
        def helper(node):
            nonlocal ans, prev
            if node == None: return
            helper(node.left)
            ans = min(ans, node.val - prev)
            prev = node.val
            helper(node.right)
        helper(root)
        return ans