# Last updated: 23/7/2025, 2:16:57 am
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return True
        
        if self.sizes[y] > self.sizes[x]:
            x, y = y, x
        self.sizes[x] += self.sizes[y]
        self.parents[y] = x
        return False

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        graph = defaultdict(dict)
        for i in range(n):
            graph[edges[i][0]][edges[i][1]] = i
        # print(graph)
        def dfs(x, vis, extra):
            for y in graph[x]:
                if y in vis:
                    extra.append(vis[y])
                    extra.append(graph[x][y])
                    continue
                vis[y] = graph[x][y]
                dfs(y, vis, extra)
        
        ans = 0
        for i in range(1, n + 1):
            vis = defaultdict(int)
            if len(graph[i]) == 0: continue
            vis[i] = -1
            extra = []
            dfs(i, vis, extra)
            # print(i, vis, extra)
            if len(vis) < n: continue
            for j in extra:
                if j == -1: continue
                un = Union(n)

                for k in range(n):
                    if k == j: continue
                    un.union(edges[k][0] - 1, edges[k][1] - 1)
                
                found = {}
                for k in range(n):
                    found[un.find(k)] = 1
                
                if len(found) == 1:
                    ans = max(ans, j)
        
        return edges[ans]

