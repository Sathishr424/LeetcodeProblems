# Last updated: 8/4/2026, 9:00:20 PM
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
13for i in range(N):
14    if is_prime[i]: primes.append(i)
15
16class Solution:
17    def divisibleGame(self, nums: list[int]) -> int:
18        n = len(nums)
19
20        factors = defaultdict(set)
21
22        for num in set(nums):
23            r_num = num
24            for p in primes:
25                if p * p > num:
26                    if num > 1: factors[r_num].add(num)
27                    break
28                if num % p == 0:
29                    factors[r_num].add(p)
30                    while num % p == 0:
31                        num //= p
32
33
34        # print(dict(factors))
35        found = []
36        for i in range(n):
37            tot = 0
38            fac = defaultdict(int)
39            for j in range(i, n):
40                tot += nums[j]
41                mx = 2
42                for d in factors[nums[j]]:
43                    fac[d] += nums[j]
44                    if fac[d] > fac[mx] or (fac[d] == fac[mx] and d < mx):
45                        mx = d
46                # print(nums[i:j+1], (i, j), dict(fac), (mx, fac[mx], tot))
47                found.append((fac[mx] - (tot - fac[mx]), -mx))
48        found.sort(reverse=True)
49        if len(found) == 0: return -sum(nums) * 2 % mod
50
51        diff, k = found[0]
52        return diff * (-k) % mod
53
54