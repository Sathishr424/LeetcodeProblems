# Last updated: 4/2/2026, 11:07:33 PM
1class Solution:
2    def maximumAmount(self, coins: List[List[int]]) -> int:
3        m = len(coins)
4        n = len(coins[0])
5
6        @cache
7        def rec(i, j, rem):
8            if i == m-1 and j == n-1: return 0
9
10            ans = -inf
11            if i+1 < m:
12                if coins[i + 1][j] < 0 and rem:
13                    ans = max(ans, rec(i + 1, j, rem - 1))
14                ans = max(ans, rec(i + 1, j, rem) + coins[i + 1][j])
15            if j+1 < n:
16                if coins[i][j + 1] < 0 and rem:
17                    ans = max(ans, rec(i, j + 1, rem - 1))    
18                ans = max(ans, rec(i, j + 1, rem) + coins[i][j + 1])
19            
20            return ans
21
22        ans = rec(0, 0, 2) + coins[0][0]
23        if coins[0][0] < 0:
24            ans = max(rec(0, 0, 1), ans)
25        
26        rec.cache_clear()
27        return ans