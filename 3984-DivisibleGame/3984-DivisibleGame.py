# Last updated: 8/4/2026, 9:37:14 PM
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
20        facts = set()
21        for num in set(nums):
22            for p in primes:
23                if p * p > num:
24                    if num > 1: facts.add(num)
25                    break
26                while num % p == 0:
27                    facts.add(p)
28                    num //= p
29        
30        best = -inf
31        best_k = inf
32        for k in facts:
33            curr = -inf
34            for num in nums:
35                add = num if num % k == 0 else -num
36                curr = max(add, curr + add)
37
38                if curr > best or (curr == best and k < best_k):
39                    best = curr
40                    best_k = k
41        
42        if best_k == inf: return -min(nums) * 2 % mod
43        # print(best_k, best)
44        return best * best_k % mod