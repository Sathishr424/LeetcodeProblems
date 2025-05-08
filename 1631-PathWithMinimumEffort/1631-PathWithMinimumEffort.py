# Last updated: 8/5/2025, 11:15:54 am
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
        
        def isGood(diff):
            q = deque([(0, 0)])
            visited = [[False] * n for _ in range(m)]

            while q:
                i, j = q.popleft()
                if i == m-1 and j == n-1: return True

                for ni, nj in DIR:
                    ni += i
                    nj += j
                    
                    if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and abs(heights[i][j] - heights[ni][nj]) <= diff:
                        visited[ni][nj] = True
                        q.append((ni, nj))
            
            return False
        
        l = 0
        r = maxi-mini

        while l < r:
            mid = (l+r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1
        
        return l