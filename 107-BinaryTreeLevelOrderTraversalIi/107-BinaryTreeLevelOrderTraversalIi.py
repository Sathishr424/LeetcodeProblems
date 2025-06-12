# Last updated: 12/6/2025, 5:53:09 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        def rec(node, level):
            if node == None: return
            if len(ret) <= level:
                ret.append([node.val])
            else:
                ret[level].append(node.val)
            rec(node.left, level+1)
            rec(node.right, level+1)
        rec(root, 0)
        return ret[::-1]