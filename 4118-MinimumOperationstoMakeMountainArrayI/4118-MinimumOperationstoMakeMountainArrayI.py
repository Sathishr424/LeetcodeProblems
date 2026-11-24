# Last updated: 11/24/2026, 5:32:15 PM
1class Solution:
2    def minOperations(self, nums: list[int]) -> int:
3        n = len(nums)
4        if n < 3: return -1
5        mx = max(nums) + n
6
7        def build():
8            dp = [[inf for _ in range(mx)] for _ in range(n)]
9            for num in range(1, mx):
10                dp[0][num] = max(0, nums[0] - num)
11
12            for i in range(1, n-1):
13                for num in range(i+1, mx):
14                    dp[i][num] = min(dp[i][num - 1], dp[i - 1][num - 1] + abs(nums[i] - num))
15            return dp
16
17        def getAns():
18            left = build()
19            best = inf
20            dp = [inf for _ in range(mx)]
21            for num in range(1, mx):
22                dp[num] = max(0, nums[n-1] - num)
23
24            for i in range(n-2, 0, -1):
25                prev = dp[n-i-1]
26                dp[n-i-1] = inf
27                for num in range(n-i, mx):
28                    tmp = dp[num]
29                    dp[num] = min(dp[num - 1], prev + abs(nums[i] - num))
30
31                    best = min(best, abs(nums[i] - num) + left[i-1][num-1] + prev)
32                    prev = tmp
33            
34            return best
35
36        return getAns()