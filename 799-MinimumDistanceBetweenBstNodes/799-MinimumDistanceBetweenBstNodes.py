# Last updated: 12/6/2025, 5:46:38 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        prev = None
        def rec(node):
            nonlocal ans, prev
            if node == None: return
            rec(node.left)
            if prev != None:
                ans = min(ans, abs(prev - node.val))
            prev = node.val
            rec(node.right)
        rec(root)
        return ans