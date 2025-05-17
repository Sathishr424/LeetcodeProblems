# Last updated: 18/5/2025, 3:38:21 am
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
        self.parents[y] = self.parents[x]
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(dict)
        sorted_edges = sorted(edges, key=lambda x: x[2])

        for x, y, w in edges:
            graph[x][y] = w
            graph[y][x] = w

        def processMst(f, t):
            uf = Union(n)
            mst = 0
            e = 1
            for x, y, w in sorted_edges:
                if (x == f and y == t) or uf.union(x, y): continue
                mst += w
                e += 1
                if e == n: break
            return mst
        
        left = []
        right = []
        min_mst = processMst(-1, -1)

        for i, (x, y, w) in enumerate(edges):
            mst = processMst(x, y)
            if mst != min_mst:
                left.append(i)
            else:
                uf = Union(n)
                uf.union(x, y)
                new_mst = w
                e = 1
                for x2, y2, w2 in sorted_edges:
                    if uf.union(x2, y2): continue
                    new_mst += w2
                    e += 1
                    if e == n: break
                if new_mst == min_mst: right.append(i)

        return [left, right]