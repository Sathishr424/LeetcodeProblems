# Last updated: 18/5/2025, 1:08:05 pm
mod = 10**9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        colors = [0, 1, 2]

        N = 0
        for i in range(1, m+1):
            N = N * 3 + (i % 2 + 1)
        N += 1

        dp = [[0] * N for _ in range(n)]

        def generatePaths(comb, index):
            if index == m:
                dp[0][comb] = 1
                return
            
            prev = comb % 3
            for color in colors:
                if index > 0 and color == prev: continue
                generatePaths(comb * 3 + color, index+1)
        
        @cache
        def possiblePaths(comb, index, st):
            if index == 0:
                return [st]
            ans = []
            prev = comb % 3
            for color in colors:
                if color == prev or (color == st % 3 and index < m): continue
                ans += possiblePaths(comb // 3, index-1, st * 3 + color)
            return ans

        generatePaths(0, 0)
        fromTo = defaultdict(list)
        for path in range(N):
            if dp[0][path]:
                fromTo[path] = possiblePaths(path, m, 0)

        for i in range(1, n):
            for from_path in range(N):
                for to_path in fromTo[from_path]:
                    dp[i][to_path] += dp[i-1][from_path]
                    dp[i][to_path] %= mod
        
        ret = 0
        for path in range(N):
            ret += dp[-1][path]
            ret %= mod

        return ret