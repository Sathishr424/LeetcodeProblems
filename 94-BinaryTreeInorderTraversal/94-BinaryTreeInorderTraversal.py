# Last updated: 12/6/2025, 5:53:26 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def dfs(node):
            if node == None: return
            dfs(node.left)
            ret.append(node.val)
            dfs(node.right)
            return ret
        dfs(root)
        return ret