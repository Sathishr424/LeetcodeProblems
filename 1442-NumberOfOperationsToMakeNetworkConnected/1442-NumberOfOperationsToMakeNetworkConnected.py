# Last updated: 12/6/2025, 5:42:21 am
class Union:
    def __init__(self, n):
        self.parents = []
        for i in range(n):
            self.parents.append(i)
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 == root2: return 1

        self.parents[root2] = root1
        return 0

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = Union(n)
        ans = 0
        cnt = 0
        for x, y in connections:
            cnt += uf.union(x, y)

        for i,p in enumerate(uf.parents):
            if i == p: ans += 1
        ans -= 1

        return ans if cnt >= ans else -1