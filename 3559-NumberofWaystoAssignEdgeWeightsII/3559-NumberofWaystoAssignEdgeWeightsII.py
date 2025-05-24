# Last updated: 24/5/2025, 10:16:48 pm
DP_N = 10**5
mod = 10**9 + 7
dp = [[-1, -1] for _ in range(DP_N)]
def rec(index, t):
    if index == DP_N:
        return t % 2

    if dp[index][t] != -1: return dp[index][t]

    ans = (rec(index+1, (t + 1) % 2) + rec(index+1, (t + 2) % 2)) % mod
    dp[index][t] = ans
    return ans

rec(0, 0)

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        N = int(log2(n)) + 1
        logs = [[-1] * n for _ in range(N)]

        visited = [False] * (n+1)
        visited[1] = True
        depths = [0] * (n+1)
        max_depth = 0

        def dfs(x, depth):
            nonlocal max_depth
            depths[x] = depth
            max_depth = max(max_depth, depth)
            for y in graph[x]:
                if not visited[y]:
                    logs[0][y-1] = x-1
                    visited[y] = True
                    dfs(y, depth+1)
            
        dfs(1, 0)

        for i in range(1, N):
            for x in range(n):
                if logs[i-1][x] == -1: continue
                logs[i][x] = logs[i-1][logs[i-1][x]]
        
        def kthNode(x, k):
            if k == 0: return x
            for i in range(N-1, -1, -1):
                if k & 1 << i:
                    k -= 1 << i
                    x = logs[i][x]
            return x
        
        def lca(x, y):
            if x == y: return x
            for i in range(N-1, -1, -1):
                if logs[i][x] != logs[i][y]:
                    x = logs[i][x]
                    y = logs[i][y]
            
            return logs[0][x]
        
        ret = []
        for x, y in queries:
            x_depth = depths[x]
            y_depth = depths[y]
    
            if x_depth > y_depth:
                x, y = y, x
                x_depth, y_depth = y_depth, x_depth

            diff = y_depth - x_depth
            new_y = kthNode(y-1, diff)

            parent = lca(x-1, new_y) + 1

            depth = depths[x] + depths[y] - depths[parent] * 2
            ret.append(rec(DP_N - depth, 0))

        return ret
            
            
        