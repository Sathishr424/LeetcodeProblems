# Last updated: 12/6/2025, 5:48:30 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(node, h=0):
            if node == None:
                return h-1
            left = getHeight(node.left, h+1)
            right = getHeight(node.right, h+1)
            self.maxi = max((left - (h))+(right - (h)), self.maxi)
            return max(left, right)
        getHeight(root)
        return self.maxi