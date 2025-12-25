# Last updated: 12/25/2025, 7:10:58 PM
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        dp = [0] * (n + 1)
        dp[0] = 1

        coins = []
        for i in range(n):
            if numWays[i]:
                coins.append(i+1)

        used = {}
        for coin in coins:
            possible = True
            for tot in range(n-coin+1):
                if dp[tot] == 0: continue
                plus = tot + coin
                if dp[plus] + dp[tot] > numWays[plus-1]:
                    possible = False
                    break
            
            if not possible: continue
            used[coin] = 1
            for tot in range(n-coin+1):
                if dp[tot] == 0: continue
                dp[tot + coin] += dp[tot]
        
        for i in range(1, n+1):
            if dp[i] != numWays[i-1]: return []
        
        return list(used.keys())


