# Last updated: 26/5/2025, 10:08:23 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)

        max_freq = [[0] * 26 for _ in range(n)]
        ret = 0
        visited = [False] * n

        def dfs(x, vis):
            if x in vis: return False
            if visited[x]: return True

            vis[x] = 1
            visited[x] = True

            for y in graph[x]:
                if not dfs(y, vis): return False
                for i in range(26):
                    max_freq[x][i] = cmax(max_freq[x][i], max_freq[y][i])

            max_freq[x][ord(colors[x]) - 97] += 1
            
            del vis[x]
            return True
        
        for x in range(n):
            if not dfs(x, {}): return -1
            ret = cmax(ret, max_freq[x][ord(colors[x]) - 97])

        return ret