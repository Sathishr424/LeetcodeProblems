# Last updated: 26/7/2025, 6:22:51 am
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))
        
        dp = [[-1] * (maxTime + 1) for _ in range(n)]

        def dfs(node, remTime):
            if dp[node][remTime] != -1: return dp[node][remTime]
            if node == n - 1: return 0

            ans = inf
            for child, t in graph[node]:
                if remTime - t < 0: continue
                ans = min(ans, dfs(child, remTime - t) + passingFees[child])
            
            dp[node][remTime] = ans
            return ans
        
        ans = dfs(0, maxTime) + passingFees[0]
        if ans == inf: return -1
        return ans