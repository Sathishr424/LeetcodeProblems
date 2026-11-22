# Last updated: 11/23/2026, 12:31:51 AM
1class Solution:
2    def minSetBits(self, nums: list[int], k: int) -> int:
3        m = 17
4        n = len(nums)
5        tot = n-k+1
6        bits = [0] * m
7        vals = []
8
9        for i in range(n):
10            val = 0
11            for b in range(m):
12                if nums[i] & (1 << b):
13                    bits[b] += 1
14
15            if i >= k-1:
16                l = i - k
17                for b in range(m):
18                    if i >= k and nums[l] & (1 << b):
19                        bits[b] -= 1
20
21                    if bits[b] == k:
22                        val += 1 << b
23
24                if val == 0: return -1
25                vals.append(val)
26
27        def dfs(index, mask):
28            if index == tot: return 0
29            if mask & vals[index]: return dfs(index + 1, mask)
30            ans = inf
31            for b in range(m):
32                bit = 1 << b
33                if vals[index] & bit:
34                    ans = min(ans, dfs(index + 1, mask | bit) + 1)
35
36            return ans
37
38        ans = dfs(0, 0)
39        return ans