# Last updated: 16/5/2025, 8:22:42 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
N = 10**5
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(node, maxi, mini):
            if node == None: return 0

            ans = max(abs(maxi - node.val), abs(mini - node.val))
            left = traverse(node.left, max(maxi, node.val), min(mini, node.val))
            right = traverse(node.right, max(maxi, node.val), min(mini, node.val))

            return max(ans, left, right)
        
        return traverse(root, root.val, root.val)