# Last updated: 12/25/2025, 7:08:58 PM
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2: return 0

        def manhattan(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        dis = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                m = manhattan(points[i], points[j])
                dis[i][j] = m
                dis[j][i] = m
        
        def dfs(x, color, graph, colors):
            colors[x] = color
            for y in graph[x]:
                if colors[y] == -1:
                    if not dfs(y, 1 - color, graph, colors): return False
                elif colors[y] == color:
                    return False
            return True

        def isGood(mid):
            graph = [[] for _ in range(n)]
            colors = [-1] * n

            for i in range(n):
                for j in range(i+1, n):
                    if dis[i][j] < mid:
                        graph[i].append(j)
                        graph[j].append(i)

            for i in range(n):
                if colors[i] == -1:
                    if not dfs(i, 0, graph, colors): return False
            
            return True

        l = 0
        r = 10**8 * 4

        while l < r:
            mid = (l + r + 1) // 2

            if isGood(mid):
                l = mid
            else:
                r = mid - 1
        
        return l