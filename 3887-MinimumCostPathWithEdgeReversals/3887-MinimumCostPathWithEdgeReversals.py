# Last updated: 12/25/2025, 7:11:07 PM
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        reverse = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            reverse[v].append((u, w * 2))

        stack = [(0, 0)]
        dis = [inf] * n
        # dis2 = [[inf, inf] for _ in range(n)]
        while stack:
            cost, node = heapq.heappop(stack)
            # print(cost, node)
            if node == n-1: return cost

            for y, c in graph[node]:
                if dis[y] > cost + c:
                    dis[y] = cost + c
                    heapq.heappush(stack, (cost + c, y))

            for y, c in reverse[node]:
                if dis[y] > cost + c:
                    dis[y] = cost + c
                    heapq.heappush(stack, (cost + c, y))

        return -1
                