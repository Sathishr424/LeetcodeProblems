# Last updated: 24/9/2025, 5:03:30 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def getN(node):
            if node == None: return 0
            return getN(node.left) + getN(node.right) + 1
        n = getN(root)

        max_heights = [0] * n
        left_h = [0] * n
        right_h = [0] * n

        def dfs(node, level):
            if node == None: return 0

            val = node.val - 1
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            left_h[val] = left + level
            right_h[val] = right + level

            return max(left, right) + 1
        
        dfs(root, 0)

        def dfs2(node, max_height):
            if node == None: return

            val = node.val - 1

            max_heights[val] = max_height

            left = left_h[val]
            right = right_h[val]

            dfs2(node.left, max(max_height, right))
            dfs2(node.right, max(max_height, left))

        dfs2(root, 0)

        ret = []
        for node in queries:
            node -= 1
            ret.append(max_heights[node])
        
        return ret