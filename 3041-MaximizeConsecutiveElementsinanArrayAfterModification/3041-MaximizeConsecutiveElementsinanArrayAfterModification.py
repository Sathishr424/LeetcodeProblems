# Last updated: 11/20/2026, 10:25:49 AM
1class Solution:
2    def maxSelectedElements(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        freq = Counter(nums)
6        mx = max(nums)
7        mn = min(nums)
8
9        @cache
10        def rec(num, deduct, order):
11            if num > mx + 1: return 0
12            ans = 0
13            
14            if freq[num] > 0:
15                ans = rec(num + 1, 1, order) + 1
16
17            if freq[num - 1] - deduct > 0:
18                ans = max(ans, rec(num + 1, 0, 0) + 1)
19
20            if order and freq[num + 1] > 0:
21                ans = max(ans, rec(num + 1, 0, 0))
22
23            return ans
24
25        ans = 0
26        for num in range(mn, mx + 1):
27            if freq[num] > 0:
28                ans = max(ans, rec(num, 0, 1))
29
30        rec.cache_clear()
31        return ans