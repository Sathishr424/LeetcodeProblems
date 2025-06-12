# Last updated: 12/6/2025, 5:35:29 am
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for i in range(1, n):
            graph[i-1].append(i)
        
        dis = [0] * n

        def dfs():
            stack = deque([0])

            while stack:
                x = stack.popleft()
                if x == n-1: return dis[x]
                for y in graph[x]:
                    if dis[y] == 0:
                        dis[y] = dis[x] + 1
                        stack.append(y)
            return 0
            
        ret = []

        for x, y in queries:
            graph[x].append(y)
            dis = [0] * n
            ret.append(dfs())
        
        return ret


