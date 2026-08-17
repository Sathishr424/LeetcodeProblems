# Last updated: 8/17/2026, 1:14:26 PM
1class Solution:
2    def stoneGameV(self, stones: List[int]) -> int:
3        n = len(stones)
4
5        prefix = [0]
6        for stone in stones:
7            prefix.append(prefix[-1] + stone)
8
9        dp = [[-1] * n for _ in range(n)]
10        def rec(l, r):
11            if l == r:
12                return 0
13
14            if dp[l][r] != -1: return dp[l][r]
15            ans = 0
16            for i in range(l, r):
17                left = prefix[i + 1] - prefix[l]
18                right = prefix[r + 1] - prefix[i + 1]
19
20                if left > right:
21                    ans = max(ans, rec(i + 1, r) + right)
22                elif right > left:
23                    ans = max(ans, rec(l, i) + left)
24                else:
25                    ans = max(ans, max(rec(l, i), rec(i+1, r)) + left)
26
27            dp[l][r] = ans
28            return ans
29
30        ans = rec(0, n-1)
31        return ans