# Last updated: 1/10/2025, 11:40:31 am
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.minScore = [inf] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y, score):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            self.minScore[x] = min(self.minScore[x], score)
            return True

        if self.sizes[y] > self.sizes[x]:
            x, y = y, x

        self.sizes[x] += self.sizes[y]
        self.parents[y] = x
        self.minScore[x] = min(self.minScore[x], self.minScore[y], score)
        
        return False

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        un = Union(n)

        for x, y, d in roads:
            x -= 1
            y -= 1
            un.union(x, y, d)

        return un.minScore[un.find(0)]