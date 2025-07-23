# Last updated: 23/7/2025, 3:18:18 pm
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

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

        def dfs2(x, par, connection, cost):
            # print((par, x), connection, cost)
            costs[x] += cost + connection

            c = costs[x]
            ret[x] = c
            conn = connections[x]
            # print(x, 'newcost', c, cost + connection)
            for y in graph[x]:
                if y == par: continue
                conn_ = conn - connections[y]
                cost_ = c - (costs[y] + connections[y] + 1)
                # print((par, x, y), conn_, cost_, (c, conn))
                dfs2(y, x, connection + conn_, cost_)

        # print(costs)
        # print(connections)
        dfs2(0, -1, 0, 0)
        return ret
                