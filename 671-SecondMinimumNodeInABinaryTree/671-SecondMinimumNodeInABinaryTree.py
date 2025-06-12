# Last updated: 12/6/2025, 5:47:47 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        hash = {}
        arr = []
        def rec(node):
            if node == None: return

            rec(node.left)
            if node.val not in hash:
                arr.append(node.val)
            hash[node.val] = 1
            rec(node.right)
        rec(root)
        arr.sort()
        return arr[1] if len(arr) >= 2 else -1