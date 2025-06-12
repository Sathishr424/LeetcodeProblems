# Last updated: 12/6/2025, 5:51:06 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        def rec(node, st):
            if node == None: return
            st += str(node.val)
            if not node.left and not node.right:
                return ret.append(st)
            st += '->'
            rec(node.left, st)
            rec(node.right, st)
        rec(root, "")
        return ret