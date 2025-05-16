# Last updated: 16/5/2025, 3:21:54 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
          
        def helper(node):
            if p.val <= node.val and q.val >= node.val:
                return node
            elif p.val > node.val:
                return helper(node.right)
            else:
                return helper(node.left)

        return helper(root)