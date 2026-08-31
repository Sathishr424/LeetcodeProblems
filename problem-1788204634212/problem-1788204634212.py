# Last updated: 9/1/2026, 1:00:34 AM
1class Solution:
2    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
3        n = len(nums)
4        ratio = a / b
5
6        ans = 0
7        for i in range(n):
8            even = 0
9            odd = 0
10            for j in range(i, n):
11                if nums[j] % 2: odd += 1
12                else: even += 1
13
14                if odd > 0 and even / odd <= ratio:
15                    ans += 1
16
17        return ans