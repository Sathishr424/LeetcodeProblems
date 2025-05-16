# Last updated: 16/5/2025, 8:24:59 am
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

            return cmax(cmax(abs(maxi - node.val), abs(mini - node.val)), cmax(traverse(node.left, cmax(maxi, node.val), cmin(mini, node.val)), traverse(node.right, cmax(maxi, node.val), cmin(mini, node.val))))
        
        return traverse(root, root.val, root.val)