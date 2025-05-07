# Last updated: 7/5/2025, 11:56:25 am
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        stack = [(0, 0, 0)]

        while stack:
            time, i, j = heapq.heappop(stack)
            if i == m-1 and j == n-1: return time

            for ni, nj in DIR:
                ni += i
                nj += j

                if 0 <= ni < m and 0 <= nj < n and moveTime[ni][nj] != -1:
                    heapq.heappush(stack, (max(time, moveTime[ni][nj])+1, ni, nj))
                    moveTime[ni][nj] = -1
        
        return -1
