# Last updated: 16/5/2025, 9:57:19 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node == None: return None

            found = node.val == p.val or node.val == q.val
            left = dfs(node.left)
            if found and left: return node
            right = dfs(node.right)
            if found and right: return node

            if left and right: return node
            elif left: return left
            elif right: return right
            elif found: return node
            return None
        
        return dfs(root)

