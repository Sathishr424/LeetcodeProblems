# Last updated: 20/7/2025, 11:28:29 am
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph = defaultdict(list)
        n = len(online)

        for x, y, c in edges:
            graph[x].append((y, c))

        stack = [(-inf, 0, 0)]
        visited = {}
        while stack:
            cost, dis, x = heapq.heappop(stack)
            if x == n-1: return -cost

            if x in visited and visited[x][0] <= dis and visited[x][1] >= cost: continue
            visited[x] = [dis, cost]
            
            for y, c in graph[x]:
                if not online[y]: continue
                if dis + c > k: continue
                heapq.heappush(stack, (-min(-cost, c), dis + c, y))

        return -1