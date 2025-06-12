# Last updated: 12/6/2025, 5:43:39 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ret = []
        hash = set(to_delete)
        def dfs(node):
            if node == None: return False
            
            if dfs(node.left): node.left = None
            if dfs(node.right): node.right = None

            if node.val in hash:
                if node.left: ret.append(node.left)
                if node.right: ret.append(node.right)
                return True
            return False
        if not dfs(root): ret.append(root)
        return ret