# Last updated: 12/6/2025, 5:50:26 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def rec(node):
            if node == None: return [0, 0]
            if node in memo: return memo[node]
            left, leftChild = rec(node.left)
            right, rightChild = rec(node.right)
            
            childs = left+right
            parent = node.val+leftChild+rightChild

            if childs > parent:
                memo[node] = [childs, childs]
            else:
                memo[node] = [parent, childs]

            return memo[node]
            
        return rec(root)[0]