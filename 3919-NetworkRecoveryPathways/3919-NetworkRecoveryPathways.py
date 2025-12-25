# Last updated: 12/25/2025, 7:10:45 PM
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        graph = defaultdict(list)
        n = len(online)
        max_cost = 0
        for x, y, c in edges:
            graph[x].append((y, c))
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
                
                for y, c in graph[x]:
                    if not online[y] or c < mid: continue
                    if dis + c > k: continue
                    heapq.heappush(stack, (dis + c, y))
            
            if can:
                l = mid
            else:
                r = mid - 1
            
        return l