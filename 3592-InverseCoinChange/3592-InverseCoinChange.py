# Last updated: 23/6/2025, 4:31:19 am
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
                dp[plus] += dp[tot]
            
            if possible: used[coin] = 1
        
        for i in range(1, n+1):
            if dp[i] != numWays[i-1]: return []
        
        return list(used.keys())


