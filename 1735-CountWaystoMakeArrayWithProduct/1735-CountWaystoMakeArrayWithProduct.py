# Last updated: 23/4/2025, 7:21:33 am
N = 10**4
mod = 10**9 + 7

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

@cache
def fact(n):
    if n <= 1: return 1
    return fact(n-1) * n % mod

def modInverse(x):
    return pow(x, -1, mod)

@cache
def getAns(cnt, n):
    a = fact(cnt+n)
    b = fact(cnt) * fact(n)
    return a * modInverse(b) % mod

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        ret = []

        for n, k in queries:
            curr = 1
            for num in primes:
                if num > k: break
                cnt = 0
                while k % num == 0:
                    cnt += 1
                    k //= num
                
                if cnt: curr = (curr * getAns(cnt, n-1)) % mod
            ret.append(curr)
        return ret