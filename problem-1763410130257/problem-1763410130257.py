# Last updated: 18/11/2025, 1:38:50 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSums = defaultdict(int)

        def dfs(node, level):
            if node == None: return
            levelSums[level] += node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        sums = sorted(levelSums.values())

        if len(sums) < k: return -1
        return sums[len(sums) - k]