# Last updated: 7/18/2026, 4:35:13 PM
1N = 10**6 + 1
2is_prime = [1] * N
3is_prime[0] = 0
4is_prime[1] = 0
5primes = []
6
7for d in range(2, int(sqrt(N)) + 1, 1):
8    if is_prime[d] == 0: continue
9    for num in range(d * d, N, d):
10        is_prime[num] = 0
11
12for num in range(2, N):
13    if is_prime[num]: primes.append(num)
14
15class Solution:
16    def findPrimePairs(self, n: int) -> List[List[int]]:
17        there = set()
18        index = bisect_right(primes, n)
19        for i in range(index):
20            num = primes[i]
21            rem = n - num
22            if is_prime[rem]:
23                x = min(rem, num)
24                if x in there: continue
25                there.add(x)
26        ret = []
27        for num in sorted(there):
28            ret.append([num, n - num])
29        return ret
30