# Last updated: 7/8/2026, 6:47:35 AM
1MOD = 10**9 + 7
2N = 10**5 + 1
3
4pows = [1] * N
5for i in range(1, N):
6    pows[i] = pows[i - 1] * 10 % MOD
7
8inv10 = pow(10, MOD - 2, MOD)   # inverse of 10
9
10inv_pows = [1] * N
11for i in range(1, N):
12    inv_pows[i] = inv_pows[i - 1] * inv10 % MOD
13
14class Solution:
15    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
16        n = len(s)
17        s = [int(d) for d in s]
18
19        sums = [0]
20        for i in range(n):
21            sums.append(sums[-1] + s[i])
22
23
24        powers = [0] * (n+1)
25        vals = [0] * (n+1)
26        cnt = 0
27        for i in range(n-1, -1, -1):
28            vals[i] = s[i] * pows[cnt] % MOD + vals[i + 1] 
29            vals[i] %= MOD
30            if s[i] > 0:
31                cnt += 1
32            powers[i] = cnt
33
34        ret = []
35        for l, r in queries:
36            sum = sums[r + 1] - sums[l]
37            val = vals[l]
38            p = powers[r + 1]
39
40            curr = val - vals[r + 1]
41
42            ans = curr * inv_pows[p] % MOD * sum % MOD
43            ret.append(ans)
44        return ret