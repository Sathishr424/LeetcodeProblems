# Last updated: 9/8/2026, 2:24:52 PM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        # 100,000
4        if n > 999:
5            return n - 999
6        return 0
7