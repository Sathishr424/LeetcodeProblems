# Last updated: 8/2/2026, 11:28:45 PM
1from functools import lru_cache
2
3class Solution:
4    def stoneGame(self, piles):
5        N = len(piles)
6
7        @lru_cache(None)
8        def dp(i, j):
9            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
10            if i > j: return 0
11            parity = (j - i - N) % 2
12            if parity == 1:  # first player
13                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
14            else:
15                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))
16
17        return dp(0, N - 1) > 0