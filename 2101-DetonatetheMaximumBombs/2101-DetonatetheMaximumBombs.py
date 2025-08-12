# Last updated: 13/8/2025, 1:02:57 am
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        def isInRange(x, y, x2, y2, r):
            return (x - x2) ** 2 + (y - y2) ** 2 <= r ** 2
        
        graph = defaultdict(list)

        def dfs(x, vis):
            if x in vis: return 0
            vis[x] = 1
            ans = 1
            for y in graph[x]:
                ans += dfs(y, vis)
            return ans
        
        for i in range(n):
            x, y, r = bombs[i]
            for j in range(n):
                if i == j: continue
                x2, y2, _ = bombs[j]

                if isInRange(x2, y2, x, y, r):
                    graph[i].append(j)
        
        ret = 1
        for i in range(n):
            ret = max(dfs(i, {}), ret)
        
        return ret
