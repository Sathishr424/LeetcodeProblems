# Last updated: 26/4/2025, 10:29:34 pm
class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(conversions) + 1
        graph = defaultdict(lambda: defaultdict(int))

        for x, y, w in conversions:
            graph[x][y] = w
        
        ret = [0] * n

        visited = [0] * n
        def dfs(x, s):
            if visited[x] == 1: return
            visited[x] = 1
            ret[x] = s
            for y in graph[x]:
                if visited[y] == 0:
                    dfs(y, s * graph[x][y] % mod)

        for i in range(n):
            dfs(i, 1)

        return ret