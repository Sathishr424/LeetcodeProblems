# Last updated: 12/6/2025, 5:45:30 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ret = TreeNode(-1)
        pointer = ret
        def rec(node):
            nonlocal pointer
            if node == None: return
            rec(node.left)
            pointer.right = TreeNode(node.val)
            pointer = pointer.right
            rec(node.right)
        rec(root)
        return ret.right