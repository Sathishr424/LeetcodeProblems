# Last updated: 29/9/2025, 4:55:02 am
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        def dfs(node, level):
            if node == None: return
            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        op = 0
        for level in levels:
            arr = levels[level]
            locations = {}
            for i in range(len(arr)):
                locations[arr[i]] = i
            
            sorted_arr = sorted(arr)

            for i in range(len(arr)):
                if arr[i] != sorted_arr[i]:
                    loc = locations[sorted_arr[i]]
                    locations[arr[i]] = loc
                    arr[i], arr[loc] = arr[loc], arr[i]
                    op += 1

        return op