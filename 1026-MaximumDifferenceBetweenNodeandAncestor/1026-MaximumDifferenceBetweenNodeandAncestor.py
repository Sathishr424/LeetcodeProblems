# Last updated: 16/5/2025, 8:23:48 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(node, maxi, mini):
            if node == None: return 0

            ans = cmax(abs(maxi - node.val), abs(mini - node.val))
            left = traverse(node.left, cmax(maxi, node.val), cmin(mini, node.val))
            right = traverse(node.right, cmax(maxi, node.val), cmin(mini, node.val))

            return cmax(ans, cmax(left, right))
        
        return traverse(root, root.val, root.val)