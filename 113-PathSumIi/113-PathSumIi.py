# Last updated: 12/6/2025, 5:53:01 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        def rec(node, path, sum):
            if node is None: return
            # print(path, sum)
            if sum+node.val == targetSum and node.left == node.right == None: 
                ret.append(path + [node.val])
            rec(node.left, path + [node.val], sum + node.val)
            rec(node.right, path + [node.val], sum + node.val)
        rec(root, [], 0)
        return ret