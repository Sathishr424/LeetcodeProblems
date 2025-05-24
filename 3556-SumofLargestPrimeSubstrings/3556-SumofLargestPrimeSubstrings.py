# Last updated: 24/5/2025, 10:19:27 pm
class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        @cache
        def isPrime(num):
            if num == 1: return False
            if num == 2: return True
            if num == 3: return True
            if num % 2 == 0: return False
            
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0: return False
            
            return True
            
        n = len(s)
        primes = {}
        for i in range(n):
            for j in range(i, n):
                num = int(s[i:j+1])
                if isPrime(num):
                    primes[num] = 1
        primes = sorted(primes.keys(), reverse=True)

        return sum(primes[:3])
                