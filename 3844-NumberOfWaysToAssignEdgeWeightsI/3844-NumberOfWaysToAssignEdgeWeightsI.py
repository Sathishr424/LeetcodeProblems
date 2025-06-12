# Last updated: 12/6/2025, 5:33:35 am
N = 10**5
mod = 10**9 + 7
dp = [[-1, -1] for _ in range(N + 1)]
def rec(index, t):
    if dp[index][t] != -1: return dp[index][t]
    if index == N:
        return t % 2

    ans = (rec(index+1, (t + 1) % 2) + rec(index+1, (t + 2) % 2)) % mod
    dp[index][t] = ans
    return ans

rec(0, 0)
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = [False] * (n+1)
        visited[1] = True
        max_depth = 0
        def dfs(x, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            for y in graph[x]:
                if not visited[y]:
                    visited[y] = True
                    dfs(y, depth+1)
            
        dfs(1, 0)

        return rec(N - max_depth, 0)

        