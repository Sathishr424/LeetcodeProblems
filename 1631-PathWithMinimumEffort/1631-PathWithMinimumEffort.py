# Last updated: 8/5/2025, 11:25:39 am
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        mini = heights[0][0]
        maxi = heights[0][0]

        for i in range(m):
            for j in range(n):
                mini = min(heights[i][j], mini)
                maxi = max(heights[i][j], maxi)
        
        def isGood(diff, i, j, vis):
            if i == m-1 and j == n-1: return True

            for ni, nj in DIR:
                ni += i
                nj += j
                
                if 0 <= ni < m and 0 <= nj < n and (ni,nj) not in vis and abs(heights[i][j] - heights[ni][nj]) <= diff:
                    vis[(ni,nj)] = 1
                    if isGood(diff, ni, nj, vis): return True
            
            return False
        
        l = 0
        r = maxi-mini

        while l < r:
            mid = (l+r) // 2

            if isGood(mid, 0, 0, {(0,0): 1}):
                r = mid
            else:
                l = mid + 1
        
        return l