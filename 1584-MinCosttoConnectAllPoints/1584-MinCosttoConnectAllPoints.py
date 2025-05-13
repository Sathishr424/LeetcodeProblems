# Last updated: 14/5/2025, 2:03:19 am
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)       

        visited = [False] * n
        v_count = 0

        min_edge = [10_000_000] * n
        min_edge[0] = 0
        heap = [(0, 0)]
        total_cost = 0
        
        while v_count < n:
            w, curr = heapq.heappop(heap)
            if visited[curr]:
                continue
    
            visited[curr] = True
            v_count += 1
            total_cost += w

            x, y = points[curr]
            for neighbor in range(n):
                if not visited[neighbor]:
                    n_x, n_y = points[neighbor]
                    cost = abs(x - n_x) + abs(y - n_y)

                    if cost < min_edge[neighbor]:
                        min_edge[neighbor] = cost
                        heapq.heappush(heap, (cost, neighbor))

        return total_cost
        
        
