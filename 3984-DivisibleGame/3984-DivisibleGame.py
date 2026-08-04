# Last updated: 8/4/2026, 9:06:06 PM
1mod = 10**9 + 7
2N = 10**6 + 1
3is_prime = [1] * N
4is_prime[0] = 0
5is_prime[1] = 0
6
7for i in range(2, int(N ** 0.5) + 1):
8    if is_prime[i] == 0: continue
9    for j in range(i * i, N, i):
10        is_prime[j] = 0
11
12primes = []
13factors = [[] for _ in range(N)]
14for i in range(N):
15    if is_prime[i]: primes.append(i)
16
17for num in range(1, N):
18    r_num = num
19    for p in primes:
20        if p * p > num:
21            if num > 1: factors[r_num].append(num)
22            break
23        if num % p == 0:
24            factors[r_num].append(p)
25            while num % p == 0:
26                num //= p
27
28inf = 10**20
29class Solution:
30    def divisibleGame(self, nums: list[int]) -> int:
31        n = len(nums)
32
33        best = -inf
34        best_k = inf
35        for i in range(n):
36            tot = 0
37            fac = defaultdict(int)
38            for j in range(i, n):
39                num = nums[j]
40                tot += num
41                mx = 2
42                for d in factors[num]:
43                    fac[d] += num
44                    if fac[d] > fac[mx] or (fac[d] == fac[mx] and d < mx):
45                        mx = d
46
47                curr = fac[mx] - (tot - fac[mx])
48                k = mx
49
50                if curr > best or (curr == best and k < best_k):
51                    best = curr
52                    best_k = k
53
54        if best_k == inf: return -sum(nums) * 2 % mod
55        return best * best_k % mod