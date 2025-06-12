# Last updated: 12/6/2025, 5:42:54 am
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dis = [0] * n
        graph = defaultdict(dict)

        for i, (x, y) in enumerate(edges):
            graph[x][y] = succProb[i]
            graph[y][x] = succProb[i]

        stack = [(-1, start_node)]

        while stack:
            prob, x = heapq.heappop(stack)
            if x == end_node: return -prob
            if dis[x] >= -prob: continue
            dis[x] = -prob

            for y in graph[x]:
                if dis[y] == 0:
                    heapq.heappush(stack, (prob * graph[x][y], y))
        
        return 0
            
        