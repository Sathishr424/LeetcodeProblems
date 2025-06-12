# Last updated: 12/6/2025, 5:41:36 am
class Solution:
    def checkIfPrerequisite(self, numCourses: int, pre: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for x,y in pre:
            graph[y].append(x)
        
        def dfs(x, vis={}):
            vis[x] = 1

            for y in graph[x]:
                if y not in vis:
                    dfs(y, vis)
            
            return vis

        memo = {}
        for i in range(numCourses):
            memo[i] = dfs(i, {})
        
        ret = []
        for x, y in queries:
            if y in memo and x in memo[y]:
                ret.append(True)
            else: ret.append(False)
        
        return ret