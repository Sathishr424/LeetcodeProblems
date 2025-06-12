# Last updated: 12/6/2025, 5:43:35 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deapest_level = 0
        deapest_node = root

        def traverse(node, level):
            nonlocal deapest_level, deapest_node
            if node == None: return level
            level += 1
            left = traverse(node.left, level)
            right = traverse(node.right, level)
            if left >= deapest_level and left == right:
                deapest_node = node
                deapest_level = left
                return left
            else:
                return max(left, right)
            

        traverse(root, 0)
        return deapest_node