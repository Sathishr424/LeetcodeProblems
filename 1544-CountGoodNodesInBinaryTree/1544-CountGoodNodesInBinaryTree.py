# Last updated: 12/6/2025, 5:41:42 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def rec(node, arr, maxi):
            if node == None: return 0
            ans = 0
            if node.val >= maxi: 
                maxi = node.val
                ans += 1
            arr.append(node.val)
            ans += rec(node.left, arr, maxi)
            ans += rec(node.right, arr, maxi)
            return ans
        
        return rec(root, [], -float('inf'))