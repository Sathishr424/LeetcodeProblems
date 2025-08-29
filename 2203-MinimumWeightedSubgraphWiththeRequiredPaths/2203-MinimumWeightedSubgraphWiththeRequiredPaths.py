# Last updated: 29/8/2025, 2:52:24 pm
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = defaultdict(list)
        reverse = defaultdict(list)

        for x, y, w in edges:
            graph[x].append((y, w))
            reverse[y].append((x, w))
        
        def dijkistra(src, graph):
            dis = [inf] * n
            heap = [(0, src)]
            while heap:
                cost, x = heapq.heappop(heap)
                if dis[x] <= cost: continue
                dis[x] = cost

                for y, w in graph[x]:
                    if cost + w < dis[y]:
                        heapq.heappush(heap, (cost + w, y))
        
            return dis
        
        from_src1 = dijkistra(src1, graph)
        from_dest = dijkistra(dest, reverse)

        dis = [inf] * n
        heap = [(0, src2)]
        min_cost = inf
        while heap:
            cost, x = heapq.heappop(heap)
            if dis[x] <= cost: continue
            dis[x] = cost
            min_cost = min(min_cost, from_src1[x] + from_dest[x] + cost)

            for y, w in graph[x]:
                if cost + w < dis[y]:
                    heapq.heappush(heap, (cost + w, y))
        
        return min_cost if min_cost != inf else -1