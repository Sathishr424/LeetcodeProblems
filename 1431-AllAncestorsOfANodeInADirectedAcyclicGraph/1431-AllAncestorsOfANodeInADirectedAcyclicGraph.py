# Last updated: 12/6/2025, 5:42:26 am
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for x, y in edges:
            graph[y].append(x)
        
        def dfs(x, vis={}, ans=[]):
            for y in graph[x]:
                if y not in vis:
                    vis[y] = 1
                    dfs(y, vis, ans)
                    ans.append(y)
            return ans
        ret = []
        for i in range(n): 
            ret.append(sorted(dfs(i, {}, [])))
        return ret
