# Last updated: 24/5/2025, 10:23:35 pm
@cache
def isPrime(num):
    if num == 1: return False
    if num == 2: return True
    if num == 3: return True
    if num % 2 == 0: return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0: return False
    
    return True

class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        n = len(s)
        primes = []
        there = {}
        for i in range(n):
            for j in range(i, n):
                num = int(s[i:j+1])
                if num in there: continue
                if isPrime(num):
                    there[num] = 1
                    heapq.heappush(primes, num)
                    if len(primes) > 3:
                        heapq.heappop(primes)
        
        return sum(primes)
                