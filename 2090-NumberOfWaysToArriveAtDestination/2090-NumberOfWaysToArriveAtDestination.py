# Last updated: 12/6/2025, 5:39:16 am
mod = 10**9 + 7
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)

        for x, y, t in roads:
            graph[x][y] = t
            graph[y][x] = t
        
        stack = [(0, 0)]

        vis = [float('inf')] * n
        distance = defaultdict(lambda: defaultdict(int))

        smallest = float('inf')

        while stack:
            t, x = heapq.heappop(stack)
            if x == n-1:
                smallest = min(smallest, t)
                continue
            
            if t >= smallest:
                continue

            for y in graph[x]:
                dis = t+graph[x][y]
                if dis <= vis[y]:
                    if dis < vis[y]:
                        heapq.heappush(stack, (dis, y))
                        vis[y] = dis
                        distance[y][dis] += distance[x][t]
                    else:
                        distance[y][dis] += distance[x][t] + 1

        return (distance[n-1][smallest]+1) % mod
