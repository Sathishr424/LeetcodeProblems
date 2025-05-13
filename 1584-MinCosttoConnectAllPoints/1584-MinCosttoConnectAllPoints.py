# Last updated: 14/5/2025, 2:02:28 am
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def mas(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        heap = [(0, 0)]
        ret = 0
        visited = [False] * n
        dis = [float('inf')] * n
        edges = 0

        while heap:
            cost, x = heapq.heappop(heap)
            if visited[x]: continue
            visited[x] = True
            ret += cost
            edges += 1
            if edges == n: break

            for y in range(n):
                if not visited[y]:
                    cost = mas(x, y)
                    if cost < dis[y]:
                        dis[y] = cost
                        heapq.heappush(heap, (cost, y))
            
        return ret