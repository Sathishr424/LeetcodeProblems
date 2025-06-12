# Last updated: 12/6/2025, 5:43:12 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def rec(node):
            if node == None: return
            rec(node.left)
            arr.append(node.val)
            rec(node.right)
        rec(root)
        n = len(arr)
        def sub(l, r):
            if l > r: return None
            mid = (l+r) // 2
            return TreeNode(arr[mid], sub(l, mid-1), sub(mid+1, r))
        return sub(0, n-1)