# Last updated: 7/5/2025, 12:51:37 pm
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
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        maxi = 0
        for i in range(n):
            for j in range(n):
                maxi = max(maxi, grid[i][j])

        l = 0
        r = maxi
        finalPos = n*n

        def isGood(mid):
            if grid[0][0] > mid: return False
            uj = Union(finalPos)
            
            for i in range(n):
                for j in range(n):
                    if grid[i][j] <= mid:
                        pos = i*n + j
                        for ni, nj in DIR:
                            ni += i
                            nj += j

                            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] <= mid:
                                uj.union(pos, ni*n + nj)
            
            return uj.find(0) == uj.find(finalPos-1)

        while l < r:
            mid = (l+r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
