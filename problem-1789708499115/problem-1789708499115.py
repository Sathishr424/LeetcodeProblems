# Last updated: 9/18/2026, 10:44:59 AM
1class Solution:
2    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
3        n = len(nums)
4        graph = [[] for _ in range(n)]
5        for i in range(1, n):
6            graph[parent[i]].append(i)
7
8        def findDepth(node):
9            level = 0
10            for child in graph[node]:
11                level = max(level, findDepth(child) + 1)
12            return level
13
14        height = findDepth(0) + 1
15
16        def calcWeight(node, depth):
17            ret = nums[node] * (height - depth + 1)
18            for child in graph[node]:
19                ret += calcWeight(child, depth + 1)
20            return ret
21
22        return calcWeight(0, 1)