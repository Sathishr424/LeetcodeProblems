# Last updated: 7/5/2025, 12:45:16 pm
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        maxi = 0
        for i in range(n):
            for j in range(n):
                maxi = max(maxi, grid[i][j])

        l = 0
        r = maxi

        def isGood(mid):
            if grid[0][0] > mid: return False
            stack = [(0, 0)]
            visited = {(0,0): 1}

            while stack:
                i, j = stack.pop()
                if i == n-1 and j == n-1: return True

                for ni, nj in DIR:
                    ni += i
                    nj += j

                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] <= mid and (ni, nj) not in visited:
                        visited[(ni, nj)] = 1
                        stack.append((ni, nj))

            return False

        while l < r:
            mid = (l+r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
