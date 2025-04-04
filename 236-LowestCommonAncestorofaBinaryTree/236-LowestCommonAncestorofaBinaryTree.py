# Last updated: 4/4/2025, 1:34:08 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found = None
        def findNode(node):
            nonlocal found
            if found: return False
            if node == None: return False

            left = findNode(node.left)
            right = findNode(node.right)

            if (node.val == p.val or node.val == q.val) and (left or right):
                found = node
                return False
            elif left and right : 
                found = node
                return False

            return left or right or node.val == q.val or node.val == p.val
        
        findNode(root)
        return found
        