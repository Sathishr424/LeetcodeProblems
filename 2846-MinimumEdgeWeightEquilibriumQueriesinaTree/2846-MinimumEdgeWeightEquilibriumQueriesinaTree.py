# Last updated: 17/5/2025, 4:19:41 am
N = 14
cmax = lambda x, y: x if x > y else y
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(dict)
        max_w = 0

        for x, y, w in edges:
            graph[x][y] = w
            graph[y][x] = w
            max_w = cmax(max_w, w)
        
        max_w += 1
        
        freq = [[0] * max_w for _ in range(n)]
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
                    for i in range(1, max_w):
                        freq[y][i] += freq[x][i]
                    freq[y][graph[x][y]] += 1
                    dfs(y, depth+1)

        dfs(root, 0)
        N = int(log2(max(depths) + 1)) + 1

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
            if x == y: return x
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

            ancestor = lca(x, new_y)
            
            for i in range(1, max_w):
                curr = (freq[x][i] + freq[y][i]) - (freq[ancestor][i] * 2)
                maxi = cmax(maxi, curr)
                total += curr

            ret.append(total - maxi)

        return ret