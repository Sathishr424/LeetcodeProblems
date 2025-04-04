# Last updated: 4/4/2025, 2:07:11 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(node, level):
            if node == None: return level-1
            return max(rec(node.left, level+1), rec(node.right, level+1))
        
        max_level = rec(root, 0)
        
        def rec2(node, level):
            if node == None: return None

            if level == max_level: return node

            left = rec2(node.left, level+1)
            right = rec2(node.right, level+1)
            
            if left and right: return node
            elif left: return left
            elif right: return right
            
            return None
        
        return rec2(root, 0)
        