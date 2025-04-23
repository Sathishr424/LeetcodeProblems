# Last updated: 23/4/2025, 6:48:32 am
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
    return (fact(n-1) * n)

@cache
def getAns(cnt, n):
    return fact(cnt+n-1) // (fact(cnt) * fact(n-1)) % mod

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        ret = []

        # 4, 8
        # ****
        # (1, 2, 4, 8, 16, 32)
        # 4, 8

        # |||||||222

        # 23||
        # 00222
        # 02022, 20022, 20202


        # 20022

        # 123, 132, 213, 231, 312, 321

        # 23|, 2|3 3|2

        for n, k in queries:
            curr = 1
            for num in primes:
                cnt = 0
                if num > k: break
                while k % num == 0:
                    cnt += 1
                    k //= num
                
                if cnt: curr = (curr * getAns(cnt, n)) % mod
            ret.append(curr)
        return ret

        