# Last updated: 16/5/2025, 10:37:32 am
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
        
        def dfs(node):
            if node == None: return None

            if node == p or node == q:
                return node
            
            left = dfs(node.left) if node.val >= p.val else None
            right = dfs(node.right) if node.val <= q.val else None

            return left and right and node or left or right or None
        
        return dfs(root)

