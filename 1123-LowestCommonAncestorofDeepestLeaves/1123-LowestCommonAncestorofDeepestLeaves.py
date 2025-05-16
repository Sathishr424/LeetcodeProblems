# Last updated: 16/5/2025, 8:47:21 am
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
            level += 1
            if node.left and node.right:
                left = traverse(node.left, level)
                right = traverse(node.right, level)
                if left == right and left >= deapest_level:
                    deapest_node = node
                    deapest_level = left
                    return left
                else:
                    return max(left, right)
            elif node.left:
                if level > deapest_level:
                    deapest_node = node.left
                    deapest_level = level
                return traverse(node.left, level)
            elif node.right:
                if level > deapest_level:
                    deapest_node = node.right
                    deapest_level = level
                return traverse(node.right, level)
            else:
                return level-1
            

        traverse(root, 0)
        return deapest_node