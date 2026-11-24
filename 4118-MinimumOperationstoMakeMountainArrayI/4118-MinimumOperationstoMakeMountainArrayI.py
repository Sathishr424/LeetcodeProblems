# Last updated: 11/24/2026, 5:28:25 PM
1class Solution:
2    def minOperations(self, nums: list[int]) -> int:
3        n = len(nums)
4        if n < 3: return -1
5        mx = max(nums) + n
6
7        def build(nums):
8            dp = [[inf for _ in range(mx)] for _ in range(n)]
9            for num in range(1, mx):
10                dp[0][num] = max(0, nums[0] - num)
11
12            for i in range(1, n-1):
13                for num in range(i+1, mx):
14                    dp[i][num] = min(dp[i][num - 1], dp[i - 1][num - 1] + abs(nums[i] - num))
15            return dp
16
17        def getAns(nums, left):
18            best = inf
19            dp = [inf for _ in range(mx)]
20            for num in range(1, mx):
21                dp[num] = max(0, nums[n-1] - num)
22
23            for i in range(n-2, 0, -1):
24                prev = dp[n-i-1]
25                dp[n-i-1] = inf
26                for num in range(n-i, mx):
27                    tmp = dp[num]
28                    dp[num] = min(dp[num - 1], prev + abs(nums[i] - num))
29
30                    best = min(best, abs(nums[i] - num) + left[i-1][num-1] + prev)
31                    prev = tmp
32            
33            return best
34
35        left = build(nums)
36        return getAns(nums, left)