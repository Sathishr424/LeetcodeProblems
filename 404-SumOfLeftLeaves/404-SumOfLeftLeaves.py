# Last updated: 12/6/2025, 5:49:50 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def rec(node, left=False):
            nonlocal ret
            if node == None: return

            rec(node.left, True) 
            rec(node.right, False)

            ret += node.val * (left and not node.left and not node.right)
            
            return False
        
        rec(root)
        return ret