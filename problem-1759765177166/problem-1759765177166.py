# Last updated: 6/10/2025, 9:09:37 pm
N = 10**5 + 1
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

def distinctPrimeFactor(num):
    if num < N and is_prime[num]: return 1
    cnt = 0
    for p in primes:
        if p * p > num:
            if num != 1:
                cnt += 1
            break
        elif num % p == 0:
            cnt += 1
            while num % p == 0:
                num //= p
    return cnt

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # nums = [1000 for _ in range(10 ** 4)]
        p = 1
        for num in nums:
            p *= num

        return distinctPrimeFactor(p)