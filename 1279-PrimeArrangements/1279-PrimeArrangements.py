# Last updated: 12/6/2025, 5:43:15 am
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 10**9 + 7

        def getPrimeNumbers(n):
            prime = [1] * (n+1)
            prime[0] = prime[1] = False
            i = 2
            while i*i <= n:
                if prime[i]:
                    for j in range(i*i, n+1, i):
                        prime[j] = 0
                i += 1
            ret = 0
            for i in range(2, n+1):
                ret += prime[i]
            return ret
        memo = {1: 1}
        def fact(i):
            if i <= 1: return 1
            elif i in memo: return memo[i]
            memo[i] = (i * fact(i-1)) % mod
            return memo[i]
        m = getPrimeNumbers(n)
        
        return (fact(m) * fact(n-m)) % mod