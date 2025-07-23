# Last updated: 23/7/2025, 3:37:24 pm
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ret = [0] * n
        costs = [0] * n
        connections = [0] * n

        def dfs(x, par):
            cost = 0
            conn = 0
            for y in graph[x]:
                if y == par: continue
                c, cn = dfs(y, x)
                cost += c + cn + 1
                conn += cn + 1
            costs[x] = cost
            connections[x] = conn
            return cost, conn
        
        dfs(0, -1)

        def reroot(x, par, connection, cost):
            costs[x] += cost + connection

            c = costs[x]
            ret[x] = c
            conn = connections[x]
            for y in graph[x]:
                if y == par: continue
                conn_ = conn - connections[y]
                cost_ = c - (costs[y] + connections[y] + 1)
                reroot(y, x, connection + conn_, cost_)


        reroot(0, -1, 0, 0)
        return ret
                