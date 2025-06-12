# Last updated: 12/6/2025, 5:49:49 am
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False
        n = len(stones)
        hash = {}
        for i in range(n):
            hash[stones[i]] = i
        dp = [{} for _ in range(n)]
        dp[1][1] = 1
        for i in range(1, n-1):
            for k in dp[i]:
                for l in range(max(1,k-1),k+2):
                    if stones[i]+l in hash:
                        dp[hash[stones[i]+l]][l] = 1
        return len(dp[-1]) > 0