# Last updated: 16/9/2025, 10:43:45 pm
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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        un = Union(n)

        for x, y in edges:
            un.union(x, y)

        ret = 0
        conn = {}
        for i in range(n):
            conn[un.find(i)] = 1
        
        cnt = 0
        for c in conn:
            ret += cnt * un.sizes[c]
            cnt += un.sizes[c]
            
        return ret