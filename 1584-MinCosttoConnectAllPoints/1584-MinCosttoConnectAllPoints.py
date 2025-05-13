# Last updated: 14/5/2025, 1:11:13 am
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = Union(n)
        graph = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j: continue
                x2, y2 = points[j]

                graph.append((abs(x1-x2) + abs(y1-y2), (i, j)))
        
        graph.sort(key=lambda x: x[0])
    
        ret = 0
        for cost, (x, y) in graph:
            if uf.union(x, y): continue
            ret += cost
        
        return ret