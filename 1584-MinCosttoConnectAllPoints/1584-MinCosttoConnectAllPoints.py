# Last updated: 14/5/2025, 1:41:22 am
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n

        def mas(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        heap = [(0, 0)]
        ret = 0
        edges = set([i for i in range(n)])
        while heap:
            cost, x = heapq.heappop(heap)
            if visited[x]: continue
            ret += cost
            edges.remove(x)
            visited[x] = True

            for y in edges:
                if visited[y]: continue
                heapq.heappush(heap, (mas(x, y), y))
            
        return ret