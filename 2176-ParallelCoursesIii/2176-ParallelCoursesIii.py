# Last updated: 12/6/2025, 5:39:00 am
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(dict)
        for x, y in relations:
            graph[y][x] = 1

        memo = [0] * (n+1)
        def dfs(x):
            if memo[x]: return memo[x]
            ans = 0
            for y in graph[x]:
                ans = max(ans, dfs(y))
            memo[x] = ans + time[x-1]
            return memo[x]
        
        return max([dfs(i+1) for i in range(n)])