# Last updated: 12/6/2025, 5:40:37 am
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        stack = [(0, 0, 0)]
    
        while stack:
            diff, i, j = heapq.heappop(stack)
            if i == m-1 and j == n-1: return diff

            if dist[i][j] < diff: continue

            h = heights[i][j]

            for ni, nj in DIR:
                ni += i
                nj += j

                if 0 <= ni < m and 0 <= nj < n:
                    currDiff = max(diff, abs(h-heights[ni][nj]))
                    if currDiff < dist[ni][nj]:
                        dist[ni][nj] = currDiff
                        heapq.heappush(stack, (currDiff, ni, nj))
        
        return dist[-1][-1]