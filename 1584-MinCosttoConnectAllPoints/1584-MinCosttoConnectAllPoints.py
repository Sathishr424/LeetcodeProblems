# Last updated: 16/5/2025, 7:27:36 am
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def getDistance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        stack = [(0, 0)]
        edges = 0
        visited = [False] * n
        total_cost = 0

        while stack:
            cost, x = heapq.heappop(stack)
            if visited[x]: continue

            visited[x] = True
            total_cost += cost
            edges += 1
            if edges == n: return total_cost

            for y in range(n):
                if visited[y]: continue
                d = getDistance(x, y)
                heapq.heappush(stack, (d, y))
        
        return total_cost