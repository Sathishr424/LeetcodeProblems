# Last updated: 25/7/2025, 4:11:22 am
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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        m = len(edgeList)
        edgeList.sort(key=lambda x: x[2])

        sort_queries = []
        for i, q in enumerate(queries):
            sort_queries.append((q, i))
        sort_queries.sort(key=lambda x: x[0][2])

        un = Union(n)
        index = 0

        ret = [False] * len(queries)
        for (x, y, limit), i in sort_queries:
            while index < m and edgeList[index][2] < limit:
                un.union(edgeList[index][0], edgeList[index][1])
                index += 1

            ret[i] = un.find(x) == un.find(y)
        
        return ret