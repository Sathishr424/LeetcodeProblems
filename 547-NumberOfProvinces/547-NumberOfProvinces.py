# Last updated: 12/6/2025, 5:48:29 am
class Solution:
    def findCircleNum(self, conn: List[List[int]]) -> int:
        visited = {}

        def dfs(x):
            if x in visited: return
            visited[x] = 1
            
            for y in range(len(conn[i])):
                if conn[x][y] == 1: dfs(y)
            
        ret = 0
        for i in range(len(conn)):
            if i not in visited:
                ret += 1
                dfs(i)

        return ret