# Last updated: 13/7/2025, 4:25:53 pm
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
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: x[2])
        un = Union(n)
        valid_edges = []
        for x, y, w in edges:
            if not un.union(x, y):
                valid_edges.append((x, y, w))
        # print(valid_edges)
        connected = {}

        for i in range(n):
            connected[un.find(i)] = 1

        rem = k - len(connected)
        
        return valid_edges[len(valid_edges) - rem - 1][2] if rem < len(valid_edges) else 0



                