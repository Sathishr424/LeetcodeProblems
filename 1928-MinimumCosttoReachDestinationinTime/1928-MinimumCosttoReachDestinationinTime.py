# Last updated: 26/7/2025, 6:20:53 am
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = defaultdict(list)
        lastNode = 0
        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))
            lastNode = max(lastNode, x, y)
        
        @cache
        def dfs(node, remTime):
            if node == lastNode: return 0

            ans = inf
            for child, t in graph[node]:
                if remTime - t < 0: continue
                ans = min(ans, dfs(child, remTime - t) + passingFees[child])
            
            return ans
        
        ans = dfs(0, maxTime) + passingFees[0]
        if ans == inf: return -1
        return ans