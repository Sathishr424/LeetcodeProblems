# Last updated: 4/4/2025, 1:47:23 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findNode(node):
            if node == None: return None

            left = findNode(node.left)
            right = findNode(node.right)

            if node.val == q.val or node.val == p.val: return node

            if left and right: return node
            elif left: return left
            elif right: return right
            
            return None
        
        return findNode(root)
        