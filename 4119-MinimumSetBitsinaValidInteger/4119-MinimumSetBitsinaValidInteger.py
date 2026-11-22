# Last updated: 11/23/2026, 12:03:35 AM
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
41            # print(index, mask, bits)
42            if index == tot: return bits
43            if mask & vals[index]: return dfs(index + 1, mask, bits)
44            ans = inf
45            change = False
46            for b in range(m):
47                bit = 1 << b
48                if mask & bit == 0 and vals[index] & bit:
49                    change = True
50                    ans = min(ans, dfs(index + 1, mask | bit, bits + 1))
51
52            # if not change: 
53            #     print("Not change:", bits, mask)
54            #     ans = min(ans, bits)
55            return ans
56
57        ans = dfs(0, 0, 0)
58        return ans