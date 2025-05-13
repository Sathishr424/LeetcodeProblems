# Last updated: 14/5/2025, 1:43:28 am
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def mas(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        heap = [(0, 0)]
        ret = 0
        edges = set([i for i in range(n)])

        while heap:
            if len(edges) == 0: break
            cost, x = heapq.heappop(heap)
            if x not in edges: continue
            ret += cost
            edges.remove(x)

            for y in edges:
                heapq.heappush(heap, (mas(x, y), y))
            
        return ret