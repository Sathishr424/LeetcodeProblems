# Last updated: 18/11/2025, 2:06:22 am
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
        if n == 1: return -1
        factors = [[] for _ in range(n)]
        left = defaultdict(int)
        right = defaultdict(int)

        for i in range(n):
            factors[i] = getPrimeFactors(nums[i])
            if i > 0:
                for p, cnt in factors[i]:
                    right[p] += cnt

        for p, cnt in factors[0]:
            left[p] += cnt
        
        for p in left:
            if right[p] != 0:
                break
        else:
            return 0
        
        for i in range(n-2):
            can = True
            for p, cnt in factors[i + 1]:
                left[p] += cnt
                right[p] -= cnt
            # print(i, dict(left), dict(right))
            for p in left:
                if right[p] != 0:
                    break
            else:
                return i + 1

        return -1
        