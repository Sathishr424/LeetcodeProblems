# Last updated: 16/5/2025, 5:31:05 am
mod = 10**9 + 7
N = 213
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        combCounts = defaultdict(int)
        dp = [[0] * N for _ in range(n)]

        @cache
        def neightborsCnt(comb, index, st):
            if index == 0: return [st]
            ans = []
            c = comb % 3

            for color in range(3):
                if color == c or (index != m and st % 3 == color): continue
                ans += neightborsCnt(comb // 3, index-1, st * 3 + color)
            
            return ans
        
        graphs_cache = [[]] * 360

        def generateIntial(comb, index):
            if index == m:
                graphs_cache[comb] = neightborsCnt(comb, m, 0)
                combCounts[comb] = len(graphs_cache[comb])
                dp[0][comb] = 1
                return
            
            prev = comb % 3
            for color in range(3):
                if color == prev: continue
                generateIntial(comb * 3 + color, index+1)

        generateIntial(0, 1)
        generateIntial(1, 1)
        generateIntial(2, 1)

        for i in range(1, n):
            for j in range(N):
                for comb in graphs_cache[j]:
                    dp[i][comb] = (dp[i][comb] + dp[i-1][j]) % mod
        
        ret = 0
        for j in range(N):
            ret = (ret + dp[n-1][j]) % mod

        return ret
        