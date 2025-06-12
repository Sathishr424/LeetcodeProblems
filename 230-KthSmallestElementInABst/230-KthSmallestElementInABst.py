# Last updated: 12/6/2025, 5:51:18 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node):
            nonlocal k
            if node == None: return None
            found = helper(node.left)
            if found: return found
            k -= 1
            if k == 0: return node
            return helper(node.right)
        return helper(root).val