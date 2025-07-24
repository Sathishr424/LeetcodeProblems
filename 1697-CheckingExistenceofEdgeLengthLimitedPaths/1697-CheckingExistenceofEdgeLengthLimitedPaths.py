# Last updated: 25/7/2025, 4:17:02 am
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return True

        if self.sizes[y] > self.sizes[x]:
            x, y = y, x

        self.sizes[x] += self.sizes[y]
        self.parents[y] = x
        
        return False
cmax = lambda x, y: x if x > y else y
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = [-1] * n
        edgeList.sort(key=lambda x: x[2])
        graph = [{} for _ in range(n)]
        main_parents = [-1] * n
        depths = [0] * n

        un = Union(n)
        for x, y, d in edgeList:
            if un.union(x, y): continue
            graph[x][y] = d
            graph[y][x] = d
        
        def dfs(node, depth, parent, main_parent):
            depths[node] = depth
            parents[node] = parent
            main_parents[node] = main_parent

            for child in graph[node]:
                if child == parent: continue
                dfs(child, depth + 1, node, main_parent)
        
        done = [0] * n
        for i in range(n):
            par = un.find(i)
            if done[par]: continue
            dfs(par, 0, -1, par)
            done[par] = 1
        
        k = floor(log2(n)) + 1
        logs = [[[-1, 0] for _ in range(n)] for _ in range(k)]

        for i in range(n):
            if parents[i] == -1: continue
            logs[0][i][0] = parents[i]
            logs[0][i][1] = graph[parents[i]][i]
        
        for i in range(1, k):
            for j in range(n):
                if logs[i-1][j][0] == -1: continue
                logs[i][j][0] = logs[i-1][ logs[i-1][j][0] ][0]
                logs[i][j][1] = cmax(logs[i-1][j][1], logs[i-1][ logs[i-1][j][0] ][1])
        
        ret = []

        def goToDepth(x, depth):
            if depth == 0: return x, 0
            ans = 0
            for i in range(k-1, -1, -1):
                if 1 << i <= depth:
                    ans = cmax(logs[i][x][1], ans)
                    x = logs[i][x][0]
                    depth -= 1 << i
            return x, ans
        
        def meet(x, y, ans):
            if x == y: return ans
            for i in range(k-1, -1, -1):
                if logs[i][x][0] == -1: continue
                if logs[i][x][0] == logs[i][y][0]: continue
                ans = cmax(ans, cmax(logs[i][x][1], logs[i][y][1]))
                x = logs[i][x][0]
                y = logs[i][y][0]
            
            return cmax(ans, cmax(logs[0][x][1], logs[0][y][1]))

        for x, y, dis in queries:
            par = main_parents[x]
            if par == -1 or main_parents[y] != par:
                ret.append(False)
                continue
            
            x_depth = depths[x]
            y_depth = depths[y]

            if y_depth < x_depth:
                x_depth, y_depth = y_depth, x_depth
                x, y = y, x
            
            depth_need = y_depth - x_depth
            new_y, ans = goToDepth(y, depth_need)
            ans = meet(x, new_y, ans)
            ret.append(ans < dis)

        return ret