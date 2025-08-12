# Last updated: 13/8/2025, 12:56:45 am
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        def isColloide(x, y, x2, y2, r):
            # print((x, y), (x2, y2), r, (x - x2) ** 2 + (y - y2) ** 2 < r ** 2)
            return (x - x2) ** 2 + (y - y2) ** 2 <= r ** 2

        def dfs(index, vis):
            ans = 1
            vis[index] = 1
            for i in range(n):
                if i in vis: continue
                if isColloide(bombs[i][0], bombs[i][1], *bombs[index]):
                    ans += dfs(i, vis)
            return ans
        
        ret = 0
        for i in range(n):
            ret = max(ret, dfs(i, {}))
        
        return ret
