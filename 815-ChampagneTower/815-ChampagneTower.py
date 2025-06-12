# Last updated: 12/6/2025, 5:46:31 am
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured] + [0] * query_row
        for i in range(query_row):
            prev = dp[0]
            dp[0] = 0
            for j in range(i+1):
                if prev > 1:
                    dp[j+1], prev = (prev - 1) / 2, dp[j+1]
                    dp[j] += dp[j+1]
                else:
                    prev = dp[j+1]
                    dp[j+1] = 0
        return min(1, dp[query_glass])