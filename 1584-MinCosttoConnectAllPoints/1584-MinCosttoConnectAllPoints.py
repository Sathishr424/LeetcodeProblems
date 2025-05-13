# Last updated: 14/5/2025, 1:34:22 am
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ret = 0
        visited = [False] * n
        visited[0] = True
        heap = []

        def mas(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        def dfs(x):
            nonlocal ret
            for y in range(n):
                if visited[y]: continue
                heapq.heappush(heap, (mas(x, y), y))
            
            while heap and visited[heap[0][1]]:
                heapq.heappop(heap)
            
            if not heap: return
            cost, y = heapq.heappop(heap)
            visited[y] = True
            ret += cost
            return dfs(y)
        
        dfs(0)
        return ret