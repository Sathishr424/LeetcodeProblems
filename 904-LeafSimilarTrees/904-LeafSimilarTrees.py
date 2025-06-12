# Last updated: 12/6/2025, 5:45:49 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr = []
        def rec(node):
            if node == None: return True
            left = rec(node.left)
            right = rec(node.right)
            if left and right:
                arr.append(node.val)
            return False
        index = 0
        match = True
        def rec2(node):
            nonlocal index, match
            if node == None: return True
            if not match: return False
            left = rec2(node.left)
            right = rec2(node.right)
            if left and right:
                if index == len(arr) or arr[index] != node.val: match = False
                else: index += 1
            return False
        rec(root1)
        # print(arr)
        rec2(root2)
        return match and index == len(arr)
