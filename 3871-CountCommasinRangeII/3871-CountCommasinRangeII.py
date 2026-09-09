# Last updated: 9/9/2026, 5:37:01 PM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        # 5,000,000
4        
5        ans = 0
6        ans += max(0, n - 999)
7        ans += max(0, n - 999999)
8        ans += max(0, n - 999999999)
9        ans += max(0, n - 999999999999)
10        ans += max(0, n - 999999999999999)
11
12        return ans