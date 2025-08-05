# Last updated: 5/8/2025, 1:15:54 pm
N = 1000 + 1
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
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # nums = [randrange(1, N) for _ in range(10**4)]
        uniq = [0] * (max(nums) + 1)
        for num in nums:
            if is_prime[num]:
                uniq[num] = 1
                continue
            for p in primes:
                while num % p == 0:
                    num //= p
                    uniq[p] = 1
                if num == 0: break
        
        return sum(uniq)