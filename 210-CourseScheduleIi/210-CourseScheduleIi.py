# Last updated: 12/6/2025, 5:51:41 am
class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x, y in pre:
            graph[x].append(y)
        
        visited = {}
        ret = []
        def dfs(x, vis):
            nonlocal ret
            if x in vis: return False
            if x in visited: return True
            vis[x] = 1

            for y in graph[x]:
                if not dfs(y, vis): return False
            ret.append(x)
            visited[x] = 1
            del vis[x]
            return True
        
        for i in range(numCourses):
            if not dfs(i, {}): return []
        
        return ret