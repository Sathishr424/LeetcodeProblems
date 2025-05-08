# Last updated: 8/5/2025, 11:33:16 am
DIR = [(0, 1), (1, 0)]

class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
    
    def find(self, x):
        if self.parents[x] != x:
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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        endPos = m*n

        def isGood(diff):
            uf = Union(endPos)
            
            for i in range(m):
                for j in range(n):
                    pos = i*n + j
                    for ni, nj in DIR:
                        ni += i
                        nj += j

                        if 0 <= ni < m and 0 <= nj < n and abs(heights[ni][nj] - heights[i][j]) <= diff:
                            uf.union(pos, ni*n + nj)
            
            return uf.find(0) == uf.find(endPos-1)
        
        l = 0
        r = 10**6

        while l < r:
            mid = (l+r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1
        
        return l