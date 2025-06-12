# Last updated: 12/6/2025, 5:51:49 am
N = 10**6 * 5
is_prime = [True] * N
is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if not is_prime[i]: continue
    j = i*i
    while j < N:
        is_prime[j] = False
        j += i

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = 0
        for i in range(2, n):
            prime += is_prime[i]
        
        return prime