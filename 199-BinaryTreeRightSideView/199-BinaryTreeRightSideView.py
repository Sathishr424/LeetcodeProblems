# Last updated: 12/6/2025, 5:51:55 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        def helper(node, level):
            if node == None: return
            if len(levels) == level:
                levels.append(node.val)
            else:
                levels[level] = node.val
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        return levels
            