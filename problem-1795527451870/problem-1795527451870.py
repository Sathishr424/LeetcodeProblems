# Last updated: 11/24/2026, 7:07:31 PM
1class Solution:
2    def minCost(self, nums: list[int]) -> int:
3        n = len(nums)
4        @cache
5        def rec(index, odd):
6            if index == n-1:
7                return nums[-1] if odd else inf
8
9            return min(rec(index + 1, odd), rec(index + 1, odd ^ 1) + nums[index])
10        
11        ans =  rec(1, 1) + nums[0]
12        rec.cache_clear()
13        return ans