# Last updated: 23/7/2025, 7:33:23 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @cache
        def rec(node, can):
            if node == None: return 0
            ans = inf

            ans = rec(node.left, 2) + rec(node.right, 2) + 1

            if can >= 2:
                ans = min(ans, rec(node.left, can - 1) + rec(node.right, can - 1))
            elif can == 1 and (node.left or node.right):
                ans = min(ans, rec(node.left, 3) + rec(node.right, 1) + 1)
                ans = min(ans, rec(node.left, 1) + rec(node.right, 3) + 1)
            
            return ans
        
        return min(rec(root, 1), rec(root, 3) + 1)