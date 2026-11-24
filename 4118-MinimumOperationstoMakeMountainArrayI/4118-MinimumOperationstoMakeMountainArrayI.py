# Last updated: 11/24/2026, 4:55:36 PM
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
17        left = build(nums)
18        right = build(nums[::-1])
19
20        best = inf
21        for i in range(1, n-1):
22            for num in range(max(i+1, n-i), mx):
23                best = min(best, left[i-1][num-1] + right[n-i-2][num-1] + abs(num - nums[i]))
24        
25        return best