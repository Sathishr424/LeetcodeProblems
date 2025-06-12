# Last updated: 12/6/2025, 5:48:01 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        def helper(node, level):
            if node == None: return
            if len(levels) == level:
                levels.append([node.val, 1])
            else:
                levels[level][0] += node.val
                levels[level][1] += 1
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        ret = []
        for tot, cnt in levels:
            ret.append(tot/cnt)
        return ret