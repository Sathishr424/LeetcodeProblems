# Last updated: 12/6/2025, 5:51:45 am
class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in pre:
            graph[x].append(y)
        
        visited = {}
        def dfs(x, vis):
            if x in vis: return False
            if x in visited: return True
            vis[x] = 1
            for y in graph[x]:
                if not dfs(y, vis): return False
            visited[x] = 1
            del vis[x]
            return True
        
        for i in range(numCourses):
            if not dfs(i, {}): return False
        
        return True