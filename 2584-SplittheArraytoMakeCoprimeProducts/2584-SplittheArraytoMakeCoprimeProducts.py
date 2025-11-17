# Last updated: 18/11/2025, 2:38:15 am
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

@cache
def getPrimeFactors(num):
    if is_prime[num]: return [(num, 1)]
    ret = []
    for p in primes:
        if p * p > num:
            if num != 1:
                ret.append((num, 1))
            break
        if num % p == 0:
            cnt = 0
            while num % p == 0:
                cnt += 1
                num //= p
            ret.append((p, cnt))

    return ret

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        factors = [[] for _ in range(n)]
        left = defaultdict(int)
        right = defaultdict(int)

        factors[0] = getPrimeFactors(nums[0])
        for i in range(1, n):
            factors[i] = getPrimeFactors(nums[i])
            for p, cnt in factors[i]:
                right[p] += cnt

        for p, cnt in factors[0]:
            left[p] += cnt
        
        for i in range(n-1):
            for p in left:
                if right[p] != 0:
                    break
            else:
                return i
            
            for p, cnt in factors[i + 1]:
                left[p] += cnt
                right[p] -= cnt

        return -1