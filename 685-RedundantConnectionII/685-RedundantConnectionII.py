# Last updated: 23/7/2025, 2:37:37 am
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.cnt = 1
    
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
        self.cnt += 1
        return False

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        def dfs(x, vis, extra):
            for y in graph[x]:
                if y in vis:
                    extra.append(vis[y])
                    extra.append(graph[x][y])
                    continue
                vis[y] = graph[x][y]
                dfs(y, vis, extra)
        
        def findCycle(node):
            vis = defaultdict(int)
            vis[node] = -1
            extra = []
            dfs(node, vis, extra)
            ans = -1

            if len(vis) < n: return -1
            for i in extra:
                if i == -1: continue
                un = Union(n)

                for k in range(n):
                    if k == i: continue
                    un.union(edges[k][0] - 1, edges[k][1] - 1)
            
                if un.cnt == n:
                    ans = max(ans, i)
            
            return ans
        
        graph = defaultdict(dict)

        for i in range(n):
            graph[edges[i][0]][edges[i][1]] = i

        ans = 0
        for node in range(1, n + 1):
            ans = max(ans, findCycle(node))
            if ans == n-1: return edges[ans]

        return edges[ans]