# Last updated: 12/6/2025, 5:53:00 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode], right=None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        def rec(node):
            if node == None: return
            stack.append(node.val)
            rec(node.left)
            rec(node.right)
        
        rec(root)
        if root:
            root.left = None
            for val in stack[1:]:
                root.right = TreeNode(val)
                root = root.right
        
