# Last updated: 12/6/2025, 5:49:31 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sumHash = defaultdict(int)
        res = 0
        def rec(node, sum_):
            nonlocal res
            if node == None: return
            
            sum_ += node.val

            if sum_ == targetSum: res += 1
            if (sumHash[sum_ - targetSum] > 0): res += sumHash[sum_ - targetSum]

            sumHash[sum_] += 1
            
            rec(node.left, sum_)
            rec(node.right, sum_)
            
            sumHash[sum_] -= 1
           
        
        rec(root, 0)
        return res