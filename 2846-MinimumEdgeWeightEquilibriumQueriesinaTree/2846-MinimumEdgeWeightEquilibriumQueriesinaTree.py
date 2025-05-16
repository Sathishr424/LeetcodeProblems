# Last updated: 17/5/2025, 4:13:56 am
N = 14
cmax = lambda x, y: x if x > y else y
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(dict)

        for x, y, w in edges:
            graph[x][y] = w
            graph[y][x] = w
        
        freq = [[0] * 27 for _ in range(n)]
        depths = [0] * n
        parents = [-1] * n

        root = 0
        visited = [False] * n
        visited[root] = True
        def dfs(x, depth):
            depths[x] = depth

            for y in graph[x]:
                if visited[y] == False:
                    visited[y] = True
                    parents[y] = x
                    for i in range(27):
                        freq[y][i] += freq[x][i]
                    freq[y][graph[x][y]] += 1
                    dfs(y, depth+1)

        dfs(root, 0)

        logs = [[-1] * n for _ in range(N)]

        for i in range(n):
            logs[0][i] = parents[i]

        for i in range(1, N):
            for j in range(n):
                if logs[i-1][j] == -1: continue
                logs[i][j] = logs[i-1][logs[i-1][j]]

        def kthNode(x, k):
            for i in range(N-1, -1, -1):
                if k >= (1 << i):
                    k -= (1 << i)
                    x = logs[i][x]
            return x

        def lca(x, y):
            for i in range(N-1, -1, -1):
                if logs[i][x] != logs[i][y]:
                    x = logs[i][x]
                    y = logs[i][y]
            return logs[0][y]
        
        ret = []
        for x, y in queries:
            depth_x = depths[x]
            depth_y = depths[y]

            if depth_x > depth_y:
                x, y = y, x
                depth_x, depth_y = depth_y, depth_x
            
            diff = depth_y - depth_x

            new_y = kthNode(y, diff) if diff > 0 else y
            
            maxi = 0
            total = 0
            
            if x == new_y: ancestor = x
            else: ancestor = lca(x, new_y)
            
            for i in range(27):
                curr = (freq[x][i] + freq[y][i]) - (freq[ancestor][i] * 2)
                maxi = cmax(maxi, curr)
                total += curr

            ret.append(total - maxi)

        return ret