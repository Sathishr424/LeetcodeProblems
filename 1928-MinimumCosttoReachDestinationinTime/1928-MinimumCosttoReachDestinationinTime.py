# Last updated: 26/7/2025, 6:37:58 am
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]

        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))
        
        stack = [(-maxTime, passingFees[0], 0)]
        visited = [inf] * n
        ret = inf
        
        while stack:
            remTime, fee, node = heapq.heappop(stack)
            remTime *= -1

            if node == n - 1: 
                ret = min(fee, ret)
                continue
            
            if visited[node] < fee:  continue
            visited[node] = fee

            for child, t in graph[node]:
                if remTime - t < 0: continue
                heapq.heappush(stack, (-(remTime - t), fee + passingFees[child], child))
        
        if ret == inf: return -1
        return ret
