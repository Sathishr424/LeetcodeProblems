# Last updated: 27/9/2025, 8:57:09 pm
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        new_graph = defaultdict(list)
        correct_graph = defaultdict(list)
        leaf_nodes = {}

        def dfs(x, par):
            is_leaf = True
            for y in graph[x]:
                if y == par: continue
                new_graph[y].append(x)
                correct_graph[x].append(y)
                dfs(y, x)
                is_leaf = False
            if is_leaf:
                leaf_nodes[x] = 1
        
        distance = [inf] * n
        dfs(0, -1)
        def dfs2(x, dis):
            distance[x] = dis
            for y in new_graph[x]:
                dfs2(y, dis + 1)
        
        dfs2(bob, 0)

        dp = [-1] * n

        def rec(x, dis):
            if dp[x] != -1: return dp[x]
            if x in leaf_nodes:
                if dis < distance[x]:
                    return amount[x]
                elif dis == distance[x]:
                    return amount[x] // 2
                return 0

            ans = -inf
            for y in correct_graph[x]:
                ans = max(ans, rec(y, dis + 1))
            
            if dis < distance[x]:
                ans += amount[x]
            elif dis == distance[x]:
                ans += amount[x] // 2
            
            dp[x] = ans
            return ans

        return rec(0, 0)