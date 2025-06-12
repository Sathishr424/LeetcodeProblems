# Last updated: 12/6/2025, 5:53:24 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cloneNode(self, node, offset):
        if node == None: return None
        return TreeNode(node.val+offset, self.cloneNode(node.left, offset), self.cloneNode(node.right, offset))

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[None], [TreeNode(1)]]

        for i in range(2, n+1):
            dp.append([])
            for j in range(i):
                for l in dp[j]:
                    for r in dp[i-(j+1)]:
                        dp[i].append(TreeNode(j+1, l, self.cloneNode(r,j+1)))
        return dp[n]
        