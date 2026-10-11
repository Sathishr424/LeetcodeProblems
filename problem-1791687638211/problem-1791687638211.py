# Last updated: 10/11/2026, 8:30:38 AM
1N = 10**6 + 1
2is_prime = [1] * N
3is_prime[0] = 0
4is_prime[1] = 1
5primes = []
6
7for i in range(2, int(sqrt(N)) + 1):
8    if not is_prime[i]: continue
9    for p in range(i * i, N, i):
10        is_prime[p] = 0
11
12prefix = [0]
13for i in range(2, N):
14    if is_prime[i]: 
15        prefix.append(prefix[-1] + i)
16        primes.append(i)
17
18class Solution:
19    def maxPrimes(self, n: int, s: int) -> list[int]:
20        ret = []
21        tot = 0
22        for num in primes:
23            if num > n or tot + num > s: break
24            tot += num
25            ret.append(num)
26
27        return ret