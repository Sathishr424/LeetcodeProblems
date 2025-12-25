# Last updated: 12/25/2025, 7:10:53 PM
class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(x, par):
            ans = 0
            for y in graph[x]:
                if y == par: continue
                ans = max(ans, dfs(y, x) + cost[y])
            return ans

        maxScore = dfs(0, -1) + cost[0]
        cost_need = [0] * n
        ret = 0
        
        def dfs2(x, par, c):
            nonlocal ret
            # print((par, x), c)
            ans = 0
            for y in graph[x]:
                if y == par: continue
                curr = dfs2(y, x, c + cost[y]) + cost[y]
                ans = max(ans, curr)
            cost_need[x] = maxScore - (c + ans)
            for y in graph[x]:
                if y == par: continue
                if cost_need[y] != cost_need[x]:
                    ret += 1
            return ans
        
        dfs2(0, -1, cost[0])
        # print(cost_need)
        return ret