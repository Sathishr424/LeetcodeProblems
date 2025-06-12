# Last updated: 12/6/2025, 5:35:16 am
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        
        for x, y in edges1:
            graph1[x].append(y)
            graph1[y].append(x)
        for x, y in edges2:
            graph2[x].append(y)
            graph2[y].append(x)
        
        def dfs(x, par, depth, graph):
            if depth > k: return 0
            ans = 1
            for y in graph[x]:
                if y == par: continue
                ans += dfs(y, x, depth+1, graph)
            return ans

        k -= 1
        max_edges = 0
        for i in range(m):
            max_edges = max(max_edges, dfs(i, -1, 0, graph2))

        k += 1
        ret = []
        for i in range(n):
            ret.append(dfs(i, -1, 0, graph1) + max_edges)
        
        return ret
        