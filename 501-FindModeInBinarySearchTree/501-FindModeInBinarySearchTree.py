# Last updated: 12/6/2025, 5:48:52 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hash = defaultdict(int)
        mode = 1
        arr = []
        def rec(node):
            nonlocal mode, arr
            if node == None: return
            hash[node.val] += 1
            if hash[node.val] > mode:
                mode = hash[node.val]
                arr = []
            if hash[node.val] == mode:
                arr.append(node.val)
            rec(node.left)
            rec(node.right)
        rec(root)
        return arr