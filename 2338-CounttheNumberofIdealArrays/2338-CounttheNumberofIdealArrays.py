# Last updated: 23/4/2025, 4:54:45 pm
mod = 10**9 + 7
N = 10**4

is_prime = [True] * (N+1)
is_prime[0] = False
# is_prime[1] = False

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
    a = fact(cnt+n-1)
    b = fact(cnt) * fact(n-1)
    return a * modInverse(b) % mod

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ret = 0
        (2, 4, 8)
        
        # 222
        # ----

        # 11---
        # |2|22, |22|2, 2||22

        ret = 0
        
        for y in range(1, maxValue+1):
            x = y
            curr = 1
            for num in primes:
                if num > x: break
                cnt = 0
                while x % num == 0:
                    cnt += 1
                    x //= num
                if cnt: curr = curr * getAns(cnt, n) % mod

            ret = (ret + curr) % mod
        
        return ret