# Last updated: 12/6/2025, 5:43:02 am
class Solution:
    def criticalConnections(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ids = [float('inf')] * n
        low = [float('inf')] * n
        id = 0
        ret = []

        def dfs(x, parent):
            nonlocal id
            ids[x] = id
            low[x] = id
            id += 1

            for y in graph[x]:
                if y == parent: continue
                if ids[y] == float('inf'): dfs(y, x)
                
                low[x] = min(low[x], low[y])

                if low[y] > ids[x]:
                    ret.append([x, y])
        
        dfs(0, -1)
    
        return ret