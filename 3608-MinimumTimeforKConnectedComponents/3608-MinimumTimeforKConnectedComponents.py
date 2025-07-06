# Last updated: 6/7/2025, 9:38:42 am
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
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        l = 0
        r = 0

        for _, _, t in edges:
            r = max(r, t)
        
        while l < r:
            time = (l + r) // 2

            un = Union(n)

            for x, y, t in edges:
                if time < t:
                    un.union(x, y)

            connected = {}
            for i in range(n):
                parent = un.find(i)
                connected[parent] = 1
        
            if len(connected) >= k:
                r = time
            else:
                l = time + 1

        return l