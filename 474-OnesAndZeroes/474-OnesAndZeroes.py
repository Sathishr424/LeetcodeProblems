# Last updated: 12/6/2025, 5:49:08 am
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def countBin(st):
            zero = 0
            for s in st: zero += s == '0'
            return [zero, len(st)-zero] 
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = 0
        ret = 0
        for s in strs:
            a = countBin(s)
            for i in range(m, a[0]-1, -1):
                for j in range(n, a[1]-1, -1):
                    if dp[i-a[0]][j-a[1]] != -1:
                        dp[i][j] = max(dp[i][j], dp[i-a[0]][j-a[1]] + 1)
                        ret = max(ret, dp[i][j])
        return ret