# Last updated: 16/5/2025, 8:21:10 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
N = 10**5
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def traverse(node, maxi, mini):
            nonlocal ans
            if node == None: return 

            ans = max(ans, abs(maxi - node.val), abs(mini - node.val))
            traverse(node.left, max(maxi, node.val), min(mini, node.val))
            traverse(node.right, max(maxi, node.val), min(mini, node.val))
        
        traverse(root, root.val, root.val)
        return ans