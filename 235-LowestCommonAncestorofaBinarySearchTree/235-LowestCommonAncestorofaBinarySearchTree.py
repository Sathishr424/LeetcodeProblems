# Last updated: 16/5/2025, 10:25:08 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p = p.val
        q = q.val
        def dfs(node):
            if node == None: return None

            if node.val == p or node.val == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right: return node
            return left or right or None
        
        return dfs(root)

