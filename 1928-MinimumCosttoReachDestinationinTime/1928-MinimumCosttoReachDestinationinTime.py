# Last updated: 26/7/2025, 6:36:00 am
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = defaultdict(list)

        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))
        
        stack = [(-maxTime, passingFees[0], 0)]
        visited = {}
        ret = inf
        
        while stack:
            remTime, fee, node = heapq.heappop(stack)
            remTime *= -1
            # print(remTime, fee, node)
            if node == n - 1: 
                ret = min(ret, fee)
                continue

            if node in visited and visited[node] < fee: 
                # print('cant vis', remTime, fee, node)
                continue
            visited[node] = fee

            for child, t in graph[node]:
                if remTime - t < 0: 
                    # print('cant', child, remTime, t)
                    continue
                heapq.heappush(stack, (-(remTime - t), fee + passingFees[child], child))
        
        if ret == inf: return -1
        return ret
