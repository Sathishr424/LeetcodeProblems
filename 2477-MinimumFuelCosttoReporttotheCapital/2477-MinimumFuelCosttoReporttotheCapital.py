# Last updated: 30/9/2025, 6:50:01 pm
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1

        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)

        cost = 0
        def dfs(x, par):
            nonlocal cost
            passengers = 1
            for y in graph[x]:
                if y == par: continue
                passengers += dfs(y, x)
                
            cars = ceil(passengers / seats)
            cost += cars
            return passengers

        for y in graph[0]:
            dfs(y, 0)

        return cost
            