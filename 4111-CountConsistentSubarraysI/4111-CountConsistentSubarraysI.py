# Last updated: 11/15/2026, 5:59:35 PM
1class Solution:
2    def countConsistent(self, nums: list[int]) -> int:
3        n = len(nums)
4        ans = 0
5        for i in range(n):
6            curr = nums[i]
7            mn = inf
8            for j in range(i, n):
9                mn = min(mn, nums[j])
10                curr &= nums[j]
11
12                if curr == mn:
13                    ans += 1
14        return ans