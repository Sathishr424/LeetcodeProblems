# Last updated: 12/6/2025, 5:42:17 am
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            pq = [(0, start)]

            while pq:
                currentDist, u = heapq.heappop(pq)

                if currentDist > dist[u]:
                    continue

                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(pq, (dist[v], v))
            return dist

        minReachableCities = float('inf')
        city = -1

        for i in range(n):
            dist = dijkstra(i)
            reachableCities = sum(d <= distanceThreshold for d in dist)

            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                city = i

        return city