# Last updated: 6/8/2025, 1:26:48 pm
N = 10 ** 6 + 1
is_prime = [1] * N
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i * i, N, i):
        is_prime[j] = 0

primes = []
for num in range(2, N):
    if is_prime[num]:
        primes.append(num)

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        l = bisect_left(primes, left)
        r = bisect_right(primes, right)

        ret = [-1, -1, inf]
        for i in range(l + 1, r):
            diff = primes[i] - primes[i - 1]
            if diff < ret[2]:
                ret = [primes[i-1], primes[i], diff]
        
        return ret[:2]