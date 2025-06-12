# Last updated: 12/6/2025, 5:52:25 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        stack = [root]
        pre = []
        while stack:
            s = stack.pop()
            pre.append(s.val)
            if s.right: stack.append(s.right)
            if s.left: stack.append(s.left)
        return pre