# Last updated: 12/6/2025, 5:33:09 am
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        inf = float('inf')
        # 1 => buy
        # 2 => short_sell
        dp = [[[inf, inf, inf] for _ in range(n+1)] for _ in range(k+1)]

        def rec(index, state, rem):
            if dp[rem][index][state] != inf: return dp[rem][index][state]
            if rem == 0 and state == 0: return 0
            if rem < 0: return 0
            if index >= n: return 0 if state == 0 else -inf

            ans = rec(index+1, state, rem)
            if state == 0:
                ans = max(ans, rec(index+1, 1, rem) - prices[index], rec(index+1, 2, rem) + prices[index])
            elif state == 1:
                ans = max(ans, rec(index+1, 0, rem-1) + prices[index])
            elif state == 2:
                ans = max(ans, rec(index+1, 0, rem-1) - prices[index])
            dp[rem][index][state] = ans
            return ans

        return rec(0, 0, k)