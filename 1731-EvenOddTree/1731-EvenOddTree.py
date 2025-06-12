# Last updated: 12/6/2025, 5:40:48 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        levels = defaultdict(list)
        def rec(node, level):
            if node == None: return
            rec(node.left, level+1)
            levels[level].append(node.val)
            rec(node.right, level+1)
        rec(root, 0)
        # print(dict(levels))
        for i in levels.keys():
            if i % 2 == 0:
                if levels[i][0] % 2 == 0: return False
                for j in range(1, len(levels[i])):
                    if not (levels[i][j] % 2 != 0 and levels[i][j] > levels[i][j-1]): return False
            else:
                if levels[i][0] % 2: return False
                for j in range(1, len(levels[i])):
                    if not (levels[i][j] % 2 == 0 and levels[i][j] < levels[i][j-1]): return False

        return True
            