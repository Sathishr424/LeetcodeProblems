# Last updated: 9/8/2026, 2:25:18 PM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        # 100,000
4        return max(0, n - 999)
5