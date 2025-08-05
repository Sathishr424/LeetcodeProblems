# Last updated: 5/8/2025, 2:04:37 pm
N = 10 ** 5 + 1
is_prime = [1] * N
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i * i, N, i):
        is_prime[j] = False

primes = []
for i in range(N):
    if is_prime[i]:
        primes.append(i)

class Solution:
    def smallestValue(self, n: int) -> int:
        while n:
            prev_n = n
            new_n = 0
            for p in primes:
                if p > n: break
                if n % p != 0: continue
                while n % p == 0:
                    new_n += p
                    n //= p
            n = new_n
            if n == prev_n: break
        return n
        