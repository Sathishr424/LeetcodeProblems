# Last updated: 23/4/2025, 7:57:31 am
N = 10**5

is_prime = [True] * (N+1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if not is_prime[i]: continue
    for j in range(i*i, N+1, i):
        is_prime[j] = False

primes = []
for i in range(2, N+1):
    if is_prime[i]: primes.append(i)

class Solution:
    def smallestValue(self, n: int) -> int:
        if n == 4: return 4
        while not is_prime[n]:
            new_n = 0
            for num in primes:
                if num > n: break
                while n % num == 0:
                    new_n += num
                    n //= num
            n = new_n
        
        return n