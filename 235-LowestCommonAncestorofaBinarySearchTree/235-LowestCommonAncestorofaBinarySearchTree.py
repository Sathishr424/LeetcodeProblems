# Last updated: 16/5/2025, 10:39:52 am
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
                left = dfs(node.left, p.val) if p.val != node.val else node
                right = dfs(node.right, q.val) if q.val != node.val else node

                return left and right and node or left or right
            elif p.val > node.val:
                return helper(node.right)
            else:
                return helper(node.left)

        return helper(root)