# Last updated: 12/6/2025, 5:45:43 am
class Solution(object):
    def reachableNodes(self, edges, M, N):
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]: continue
            ans += 1

            for nei, weight in graph[node].iteritems():
                v = min(weight, M - d)
                used[node, nei] = v

                d2 = d + weight + 1
                if d2 < dist.get(nei, M+1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans