# Last updated: 23/9/2025, 12:20:01 am
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def getOrder(conditions):
            graph = defaultdict(list)

            for u, v in conditions:
                graph[u].append(v)
            
            order = []
            
            visited = {}
            vis = {}
            def dfs(x):
                if x in vis: return False
                if x in visited: return True
                vis[x] = 1
                visited[x] = 1
                for y in graph[x]:
                    if not dfs(y): return False
                order.append(x)
                del vis[x]
                return True
    
            for i in range(1, k + 1):
                if i not in visited:
                    if not dfs(i): return []

            return order[::-1]

        row = getOrder(rowConditions)
        if len(row) == 0: return []
        col = getOrder(colConditions)
        if len(col) == 0: return []
        
        grid = [[0] * k for _ in range(k)]

        indexes = {}
        for i, val in enumerate(row):
            indexes[val] = i
        
        for i, val in enumerate(col):
            if val in indexes:
                grid[indexes[val]][i] = val
                del indexes[val]
            else:
                grid[0][i] = val

        for val in indexes:
            grid[indexes[val]][0] = val
        
        return grid
        