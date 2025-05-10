# Last updated: 10/5/2025, 9:40:03 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = defaultdict(dict)

        for x, y, w in edges:
            graph[x][y] = w

        @cache
        def dfs(x, rem, tot):
            if rem == 0 and tot > 0: return 0
            if rem <= 0 or tot <= 0: return -float('inf')
            ans = -float('inf')
            for y in graph[x]:
                ans = cmax(ans, dfs(y, rem-1, tot-graph[x][y]) + graph[x][y])
            return ans
        
        ans = max([dfs(x, k, t) for x in range(n)])
        return cmax(-1, ans)