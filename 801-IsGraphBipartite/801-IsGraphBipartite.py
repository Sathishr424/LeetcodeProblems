# Last updated: 12/6/2025, 5:46:37 am
class Union:
    def __init__(self, n):
        self.parents = []
        self.size = []
        for i in range(n):
            self.parents.append(i)
            self.size.append(0)
        
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2: return 0

        if self.size[root1] < self.size[root2]:
            root2, root1 = root1, root2
        
        self.size[root1] += self.size[root2]
        self.parents[root2] = root1
        return 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = Union(len(graph))

        for i,g in enumerate(graph):
            for v in g:
                if uf.isConnected(i, v): return False
                uf.union(g[0], v)
        return True
