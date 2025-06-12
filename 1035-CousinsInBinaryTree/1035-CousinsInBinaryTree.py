# Last updated: 12/6/2025, 5:44:38 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        found = None
        def check(node, parent, level):
            nonlocal found
            if node == None: return False
            if node.val == x or node.val == y:
                if found: return parent.val != found[0] and level == found[1]
                found = [parent.val, level]
            return False
        
        def rec(node, level=1):
            if node == None: return False
            return check(node.left, node, level+1) or rec(node.left, level+1) or check(node.right, node, level+1) or rec(node.right, level+1)
        
        return rec(root)