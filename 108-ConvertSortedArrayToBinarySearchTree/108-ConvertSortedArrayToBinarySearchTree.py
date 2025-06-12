# Last updated: 12/6/2025, 5:53:08 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right: return None
            mid = (left+right) // 2
            return TreeNode(nums[mid], helper(left, mid-1), helper(mid+1, right))
        return helper(0, len(nums)-1)