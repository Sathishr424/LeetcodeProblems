# Last updated: 12/6/2025, 5:53:05 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node, height):
            if node == None:
                return height-1
            return max(getHeight(node.left, height+1), getHeight(node.right, height+1))
        
        def sub(node):
            if node:
                if abs(getHeight(node.left, 1) - getHeight(node.right, 1)) > 1: return False
                if not sub(node.left): return False
                if not sub(node.right): return False
                return True
            return True
        return sub(root)
            
        # return True if abs(getHeight(root.left, 1) - getHeight(root.right, 1)) <= 1 else False