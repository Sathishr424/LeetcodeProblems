# Last updated: 9/22/2026, 3:41:36 PM
1class Solution:
2    def resultArray(self, nums: List[int], k: int) -> List[int]:
3        n = len(nums)
4
5        @cache
6        def rec(index, rem, used):
7            ans = [0] * k
8            if used and rem < k:
9                ans[rem] += 1
10
11            if index == n:
12                return ans
13
14            if not used:
15                curr = rec(index + 1, rem, used)
16                for x in range(k):
17                    ans[x] += curr[x]
18
19            curr = rec(index + 1, (rem * nums[index]) % k, True)
20            for x in range(k):
21                ans[x] += curr[x]
22
23            return ans
24
25        ans = rec(0, 1, False)
26        rec.cache_clear()
27        return ans