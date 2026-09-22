# Last updated: 9/22/2026, 5:15:06 PM
1class Solution:
2    def resultArray(self, nums: List[int], k: int) -> List[int]:
3        n = len(nums)
4
5        dp = [[[0] * k for _ in range(k)] for _ in range(n + 1)]
6
7        for i in range(n):
8            dp[i + 1][nums[i] % k][nums[i] % k] += 1
9
10        ans = [0] * k
11        for i in range(n):
12            ni = i + 1
13            for rem in range(k):
14                nrem = (rem * nums[i]) % k
15                dp[ni][nrem][nrem] += dp[i][rem][rem]
16        
17        for i in range(1, n + 1):
18            for rem in range(k):
19                for x in range(k):
20                    ans[x] += dp[i][rem][x]
21
22        return ans