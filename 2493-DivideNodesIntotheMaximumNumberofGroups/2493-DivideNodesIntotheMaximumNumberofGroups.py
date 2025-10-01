# Last updated: 2/10/2025, 1:56:21 am
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

def isBipartite(graph, parents):
    vis = {}
    def dfs(x, par, level):
        vis[x] = level
        for y in graph[x]:
            if y == par: continue
            if y in vis:
                if (level - vis[y] + 1) & 1:
                    return False
            elif not dfs(y, x, level + 1): return False

        return True
    
    for node in parents:
        vis = {}
        if not dfs(node, -1, 0): return False
    
    return True

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        un = Union(n)
        for x, y in edges:
            x -= 1
            y -= 1
            un.union(x, y)
            graph[x].append(y)
            graph[y].append(x)
        
        parents = defaultdict(list)
        for i in range(n):
            parents[un.find(i)].append(i)
        
        if not isBipartite(graph, parents): return -1
        
        def bfs(node):
            stack = deque([node])

            distance = 0
            vis = [0] * n
            vis[node] = 1
            while stack:
                for _ in range(len(stack)):
                    x = stack.popleft()
                    for y in graph[x]:
                        if vis[y]: continue
                        vis[y] = 1
                        stack.append(y)
                distance += 1
                
            return distance
        
        groups = 0
        for par in parents:
            best_group = 0
            for node in parents[par]:
                distance = bfs(node)
                best_group = max(distance, best_group)
            groups += best_group
        
        return groups