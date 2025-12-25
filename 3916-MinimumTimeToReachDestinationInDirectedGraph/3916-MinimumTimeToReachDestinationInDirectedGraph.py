# Last updated: 12/25/2025, 7:10:48 PM
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(lambda: defaultdict(list))

        for x, y, s, e in edges:
            graph[x][y].append((s, e))
        
        stack = [(0, 0)]
        # 2, (3, 8)
        # 10, (3, 7)
        visited = {}
        while stack:
            t, x = heapq.heappop(stack)
            if x in visited and visited[x] <= t: continue
            visited[x] = t

            for y in graph[x]:
                for s, e in graph[x][y]:
                    # print(s, e, (x, t))
                    if t >= s and t <= e:
                        heapq.heappush(stack, (t + 1, y))
                    elif t < s:
                        heapq.heappush(stack, (t + 1 + (s - t), y))

        return visited[n-1] if n-1 in visited else -1
                        