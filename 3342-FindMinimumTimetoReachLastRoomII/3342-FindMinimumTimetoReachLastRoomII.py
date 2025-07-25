# Last updated: 8/5/2025, 10:49:34 am
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
alt_arr = [0, 2, 1]

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m = len(moveTime)
        n = len(moveTime[0])

        stack = [(0, 0, 0, 1)]
        moveTime[0][0] = -1

        while stack:
            time, i, j, alt = heapq.heappop(stack)

            for ni, nj in DIR:
                ni += i
                nj += j

                if 0 <= ni < m and 0 <= nj < n and moveTime[ni][nj] != -1:
                    newTime = max(moveTime[ni][nj], time) + alt
                    if ni == m-1 and nj == n-1: return newTime
                    heapq.heappush(stack, (newTime, ni, nj, alt_arr[alt]))
                    moveTime[ni][nj] = -1
        
        return 0