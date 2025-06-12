# Last updated: 12/6/2025, 5:33:12 am
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m  = len(grid)
        n = len(grid[0])
        ret = []
        
        def calc(i2, j2):
            dist = {}
            for i in range(i2, i2+k):
                for j in range(j2, j2+k):
                    dist[grid[i][j]] = 1
            if len(dist) == 1: return 0
            dist = sorted(dist.keys())

            ans = abs(dist[0] - dist[1])
            for i in range(1, len(dist)):
                ans = min(ans, abs(dist[i-1] - dist[i]))
            return ans
        
        for i in range(m-k+1):
            tmp = []
            for j in range(n-k+1):
                tmp.append(calc(i, j))
            ret.append(tmp)

        return ret
                