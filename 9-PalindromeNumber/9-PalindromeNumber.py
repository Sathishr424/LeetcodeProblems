# Last updated: 4/8/2025, 2:26:35 pm
N = 5 * (10 ** 6) + 2
is_prime = [True] * N
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i*i, N, i):
        is_prime[j] = False

prime_cnts = [0] * N
for i in range(1, N):
    prime_cnts[i] += prime_cnts[i - 1]
    if is_prime[i - 1]:
        prime_cnts[i] += 1

class Solution:
    def countPrimes(self, n: int) -> int:
        return prime_cnts[n]