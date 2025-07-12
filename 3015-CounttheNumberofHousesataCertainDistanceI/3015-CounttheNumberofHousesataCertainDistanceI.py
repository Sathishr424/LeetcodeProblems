# Last updated: 12/7/2025, 10:08:01 pm
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(1, n):
            graph[i].append(i + 1)
            graph[i + 1].append(i)
        
        graph[x].append(y)
        graph[y].append(x)

        ret = [0] * n

        def dfs(x, rem, vis):
            vis[x] = rem
            if rem == n: return
            for y in graph[x]:
                if y not in vis or vis[y] > rem:
                    dfs(y, rem + 1, vis)
        
        for i in range(1, n + 1):
            vis = {}
            dfs(i, 0, vis)
            for x in vis:
                if x != i:
                    ret[vis[x] - 1] += 1

        return ret