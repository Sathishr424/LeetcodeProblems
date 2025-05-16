# Last updated: 16/5/2025, 10:23:35 am
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
        
        def dfs(node, x):
            if node == None: return None
            if node.val == x: return node

            if x > node.val:
                return dfs(node.right, x)
            else:
                return dfs(node.left, x)
        
        def helper(node):
            if p.val <= node.val and q.val >= node.val:
                left = dfs(node, p.val)
                right = dfs(node, q.val)

                return left and right and node or left or right
            elif p.val > node.val:
                return helper(node.right)
            else:
                return helper(node.left)

        return helper(root)