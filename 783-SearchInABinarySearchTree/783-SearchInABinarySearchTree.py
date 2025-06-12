# Last updated: 12/6/2025, 5:46:50 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            s = stack.pop()
            if s.val == val: return s
            if val > s.val:
                if s.right: stack.append(s.right)
            else:
                if s.left: stack.append(s.left)
        
        return None
                