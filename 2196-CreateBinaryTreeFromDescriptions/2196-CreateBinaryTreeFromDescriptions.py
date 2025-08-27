# Last updated: 27/8/2025, 10:14:09 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, des: List[List[int]]) -> Optional[TreeNode]:
        founded = {}
        has_parent = {}
        
        for p, c, is_left in des:
            has_parent[c] = 1
            if p not in founded:
                founded[p] = TreeNode(p)
            
            if c not in founded:
                founded[c] = TreeNode(c)
            
            if is_left:
                founded[p].left = founded[c]
            else:
                founded[p].right = founded[c]

        for p, _, _ in des:
            if p not in has_parent:
                return founded[p]

        return None
            