# Last updated: 19/7/2025, 9:49:05 pm
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph = defaultdict(dict)
        n = len(online)
        max_cost = 0
        for x, y, c in edges:
            graph[x][y] = c
            max_cost = max(max_cost, c)
        
        l = -1
        r = max_cost
        while l < r:
            mid = (l + r + 1) // 2

            stack = [(0, 0)]
            visited = [inf] * n
            can = False
            while stack:
                dis, x = heapq.heappop(stack)
                if x == n-1:
                    can = True
                    break

                if visited[x] <= dis: continue
                visited[x] = dis
                
                for y in graph[x]:
                    if not online[y] or graph[x][y] < mid: continue
                    if dis + graph[x][y] > k: continue
                    heapq.heappush(stack, (dis + graph[x][y], y))
            
            if can:
                l = mid
            else:
                r = mid - 1
            
        return l