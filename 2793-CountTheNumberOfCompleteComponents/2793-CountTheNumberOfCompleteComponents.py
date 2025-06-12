# Last updated: 12/6/2025, 5:36:55 am
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = {}
        def dfs(x):
            stack = [x]
            vis = {x: 1}
            is_complete = True
            
            while stack:
                node = stack.pop()
                visited[node] = 1
                for y in graph[node]:
                    if y not in vis:
                        is_complete = is_complete and len(graph[node]) == len(graph[y])
                        stack.append(y)
                        vis[y] = 1
            
            return is_complete and len(graph[x]) == len(vis)-1

        ret = 0

        for x in range(n):
            if x not in visited:
                ret += dfs(x)
        
        return ret

