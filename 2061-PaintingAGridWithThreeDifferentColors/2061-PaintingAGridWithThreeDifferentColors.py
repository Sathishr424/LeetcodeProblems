# Last updated: 12/6/2025, 5:39:19 am
mod = 10**9 + 7
colors = [0, 1, 2]
N = 213
dp = [[[0] * N for _ in range(1000)] for _ in range(6)]

def processM(m):
    def generatePaths(comb, index):
        if index == m:
            dp[m][0][comb] = 1
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
        if dp[m][0][path]:
            fromTo[path] = possiblePaths(path, m, 0)

    for i in range(1, 1000):
        for from_path in range(N):
            for to_path in fromTo[from_path]:
                dp[m][i][to_path] += dp[m][i-1][from_path]
                dp[m][i][to_path] %= mod

for i in range(5):
    processM(i+1)

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        ret = 0
        for path in range(N):
            ret += dp[m][n-1][path]
            ret %= mod

        return ret