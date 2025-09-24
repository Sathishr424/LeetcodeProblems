# Last updated: 24/9/2025, 8:19:20 pm
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
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)
        new_edges = []
        for u, v in edges:
            new_edges.append((max(vals[u], vals[v]), u, v))
            new_edges.append((max(vals[u], vals[v]), v, u))
        
        new_edges.sort()
        un = Union(n)

        val_set = defaultdict(list)
        for i in range(n):
            val_set[vals[i]].append(i)

        total = 0
        prev = -1
        there = {}
        for i, (val, u, v) in enumerate(new_edges):
            if val != prev:
                pars = defaultdict(int)
                for x in val_set[prev]:
                    pars[un.find(x)] += 1
                    total += pars[un.find(x)]
            un.union(u, v)
            prev = val
            there[val] = 1
        
        pars = defaultdict(int)
        for x in val_set[prev]:
            pars[un.find(x)] += 1
            total += pars[un.find(x)]
        
        for val in val_set:
            if val not in there:
                total += len(val_set[val])

        return total