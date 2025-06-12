# Last updated: 12/6/2025, 5:45:59 am
class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)
        memo = []
        hash = {}
        for i in range(n):
            memo.append(-1)
            hash[quiet[i]] = i
        
        for x, y in richer:
            graph[y].append(x)

        def dfs(x):
            if memo[x] != -1: return memo[x]
            q = quiet[x]
            for y in graph[x]:
                q = min(q, dfs(y))
            memo[x] = q
            return q

        return [hash[dfs(i)] for i in range(n)]