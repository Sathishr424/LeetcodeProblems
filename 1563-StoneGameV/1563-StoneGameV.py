# Last updated: 8/17/2026, 1:16:33 PM
1cmax = lambda x, y: x if x > y else y
2class Solution:
3    def stoneGameV(self, stones: List[int]) -> int:
4        n = len(stones)
5
6        prefix = [0]
7        for stone in stones:
8            prefix.append(prefix[-1] + stone)
9
10        dp = [[-1] * n for _ in range(n)]
11        def rec(l, r):
12            if l == r:
13                return 0
14
15            if dp[l][r] != -1: return dp[l][r]
16            ans = 0
17            for i in range(l, r):
18                left = prefix[i + 1] - prefix[l]
19                right = prefix[r + 1] - prefix[i + 1]
20
21                if left > right:
22                    ans = cmax(ans, rec(i + 1, r) + right)
23                elif right > left:
24                    ans = cmax(ans, rec(l, i) + left)
25                else:
26                    ans = cmax(ans, cmax(rec(l, i), rec(i+1, r)) + left)
27
28            dp[l][r] = ans
29            return ans
30
31        ans = rec(0, n-1)
32        return ans