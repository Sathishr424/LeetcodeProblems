# Last updated: 5/7/2025, 9:39:50 pm
class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        stack = [(1, 0, 0, 1)]
        DIR = [(0, 1), (1, 0)]
        visited = {}
        while stack:
            cost, i, j, s = heapq.heappop(stack)
            key = (i, j, s % 2)
            if key in visited and visited[key] <= cost: continue
            visited[key] = cost
            # print(cost, (i, j), s)
            if i == m-1 and j == n-1: return cost
            
            new_cost = cost
            if s % 2 == 0:
                s += 1
                new_cost += waitCost[i][j]

            for i2, j2 in DIR:
                i2 += i
                j2 += j

                if 0 <= i2 < m and 0 <= j2 < n:
                    heapq.heappush(stack, (new_cost + (i2 + 1) * (j2 + 1), i2, j2, s + 1))

        return -1