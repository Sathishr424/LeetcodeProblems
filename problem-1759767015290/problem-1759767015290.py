# Last updated: 6/10/2025, 9:40:15 pm
N = 10**6 + 1
is_prime = [1] * N
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i * i, N, i):
        is_prime[j] = 0
        
primes = []
for i in range(N):
    if is_prime[i]:
        primes.append(i)

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ret = [-1, -1]
        prev = -1
        for i in range(left, right + 1):
            if is_prime[i]:
                if prev != -1:
                    if ret[0] == -1 or ret[1] - ret[0] > i - prev:
                        ret = [prev, i]
                prev = i

        return ret