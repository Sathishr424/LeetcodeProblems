# Last updated: 11/23/2026, 12:05:28 AM
1class Solution:
2    def minSetBits(self, nums: list[int], k: int) -> int:
3        m = 17
4        n = len(nums)
5        full = (1 << n) - 1
6        tot = n-k+1
7        bits = [0] * m
8        vals = []
9
10        for i in range(k):
11            for b in range(m):
12                if nums[i] & (1 << b):
13                    bits[b] += 1
14
15        val = 0
16        for b in range(m):
17            if bits[b] == k: 
18                val += 1 << b
19
20        if val == 0: return -1
21        vals.append(val)
22
23        for i in range(k, n):
24            val = 0
25            l = i - k
26            for b in range(m):
27                if nums[l] & (1 << b):
28                    bits[b] -= 1
29
30            for b in range(m):
31                if nums[i] & (1 << b):
32                    bits[b] += 1
33
34                if bits[b] == k:
35                    val += 1 << b
36
37            if val == 0: return -1
38            vals.append(val)
39
40        def dfs(index, mask, bits):
41            if index == tot: return bits
42            if mask & vals[index]: return dfs(index + 1, mask, bits)
43            ans = inf
44            for b in range(m):
45                bit = 1 << b
46                if vals[index] & bit:
47                    ans = min(ans, dfs(index + 1, mask | bit, bits + 1))
48
49            return ans
50
51        ans = dfs(0, 0, 0)
52        return ans