# Last updated: 9/10/2026, 1:07:58 PM
1class Solution:
2    def averageOfSubtree(self, root: TreeNode) -> int:
3        ans = 0
4        def dfs(node):
5            nonlocal ans
6            if node == None:
7                return [0, 0]
8
9            left = dfs(node.left)
10            right = dfs(node.right)
11
12            ret = [node.val + left[0] + right[0], left[1] + right[1] + 1]
13
14            if node.val == ret[0] // ret[1]:
15                ans += 1
16
17            return ret
18
19        dfs(root)
20        return ans