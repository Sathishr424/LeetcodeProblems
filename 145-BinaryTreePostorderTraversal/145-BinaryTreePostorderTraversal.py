# Last updated: 12/6/2025, 5:52:24 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def rec(node):
            if node == None: return
            rec(node.left)
            rec(node.right)
            arr.append(node.val)
        rec(root)
        return arr