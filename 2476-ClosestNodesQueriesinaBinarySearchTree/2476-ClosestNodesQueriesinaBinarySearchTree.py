# Last updated: 29/9/2025, 5:00:04 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        def dfs(node):
            if node == None: return
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        arr.sort()
        # print(arr)
        
        ret = []
        for val in queries:
            curr = [-1, -1]
            index = bisect_right(arr, val)
            if index > 0:
                curr[0] = arr[index - 1]
            index = bisect_left(arr, val)
            if index < len(arr):
                curr[1] = arr[index]
            ret.append(curr)
        
        return ret