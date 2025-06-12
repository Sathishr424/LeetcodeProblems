# Last updated: 12/6/2025, 5:53:02 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, sum):
            if node == None: return False
            if node.left == None and node.right == None: return sum-node.val == 0
            return helper(node.left, sum-node.val) or helper(node.right, sum-node.val)
        return helper(root, targetSum)