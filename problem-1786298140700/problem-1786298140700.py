# Last updated: 8/9/2026, 11:25:40 PM
1class Solution:
2    def countDominantNodes(self, root: TreeNode | None) -> int:
3        def dfs(node):
4            if node == None: return [0, -1]
5            
6            cnt = 0
7            mx = node.val
8
9            c, m = dfs(node.left)
10            cnt += c
11            mx = max(mx, m)
12
13            c, m = dfs(node.right)
14            cnt += c
15            mx = max(mx, m)
16
17            if mx == node.val:
18                cnt += 1
19
20            return [cnt, mx]
21
22        return dfs(root)[0]