# Last updated: 18/5/2025, 10:55:10 pm
class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        weights = [0] * n
        depths = [0] * n
        parents = [-1] * n
        graph = defaultdict(dict)

        for x, y, w in edges:
            graph[x][y] = w
            graph[y][x] = w

        visited = [False] * n
        visited[0] = True
        def dfs(x, w, depth):
            weights[x] = w
            depths[x] = depth
            for y in graph[x]:
                if not visited[y]:
                    parents[y] = x
                    visited[y] = True
                    dfs(y, w + graph[x][y], depth + 1)
        
        dfs(0, 0, 0)
        N = int(log2(max(depths))) + 1
        logs = [[-1] * n for _ in range(N)]

        for i in range(n):
            logs[0][i] = parents[i]
        
        for i in range(1, N):
            for x in range(n):
                if logs[i-1][x] == -1: continue
                logs[i][x] = logs[i-1][logs[i-1][x]]
        
        def kthNode(x, k):
            if k == 0: return x
            for i in range(N-1, -1, -1):
                if k >= 1 << i:
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

        def getAncestor(x, y):
            d_x = depths[x]
            d_y = depths[y]
            if d_x > d_y:
                x, y = y, x
                d_x, d_y = d_y, d_x
            
            diff = d_y - d_x
            new_y = kthNode(y, diff)
            return lca(x, new_y)

        ret = []
        for x, y, z in queries:
            ab = getAncestor(x, y)
            w = weights[x] + weights[y] - weights[ab] * 2
            bc = getAncestor(y, z)
            w += weights[y] + weights[z] - weights[bc] * 2
            ca = getAncestor(z, x)
            w += weights[z] + weights[x] - weights[ca] * 2

            ret.append(w//2)
        
        return ret

