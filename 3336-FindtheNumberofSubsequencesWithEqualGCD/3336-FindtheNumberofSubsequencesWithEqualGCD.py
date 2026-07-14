# Last updated: 7/14/2026, 2:20:51 PM
1class Solution:
2    def subsequencePairCount(self, nums: List[int]) -> int:
3        n = len(nums)
4        mod = 10**9 + 7
5
6        @cache
7        def rec(index, x, y):
8            if index == n:
9                return x == y and x > 0
10            
11            ans = rec(index + 1, gcd(x, nums[index]), y) + rec(index + 1, x, gcd(y, nums[index])) + rec(index + 1, x, y)
12            return ans % mod
13
14        ans = rec(0, 0, 0)
15        rec.cache_clear()
16        return ans