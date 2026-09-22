# Last updated: 9/22/2026, 5:17:52 PM
1class Solution:
2    def resultArray(self, nums: List[int], k: int) -> List[int]:
3        n = len(nums)
4
5        dp = [[[0] * k for _ in range(k)] for _ in range(n + 1)]
6
7        ans = [0] * k
8        for i in range(n):
9            dp[i + 1][nums[i] % k][nums[i] % k] += 1
10            ans[nums[i] % k] += 1
11
12        for i in range(n):
13            ni = i + 1
14            for rem in range(k):
15                nrem = (rem * nums[i]) % k
16                dp[ni][nrem][nrem] += dp[i][rem][rem]
17                ans[nrem] += dp[i][rem][rem]
18        
19        return ans