# Last updated: 12/6/2025, 5:48:43 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = [0, root.val]
        def rec(node, level=0):
            nonlocal ans
            if node == None: return
            rec(node.left, level+1)
            if level > ans[0]:
                ans = [level, node.val]
            rec(node.right, level+1)
        rec(root)
        return ans[1]