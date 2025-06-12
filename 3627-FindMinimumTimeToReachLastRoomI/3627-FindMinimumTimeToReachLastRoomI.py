# Last updated: 12/6/2025, 5:35:22 am
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        stack = [(0, 0, 0)]

        while stack:
            time, i, j = heapq.heappop(stack)

            for ni, nj in DIR:
                ni += i
                nj += j

                if 0 <= ni < m and 0 <= nj < n and moveTime[ni][nj] != -1:
                    newTime = max(time, moveTime[ni][nj])+1
                    if ni == m-1 and nj == n-1: return newTime
                    heapq.heappush(stack, (newTime, ni, nj))
                    moveTime[ni][nj] = -1
        
        return -1
