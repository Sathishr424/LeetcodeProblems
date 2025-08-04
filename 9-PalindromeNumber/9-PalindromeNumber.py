# Last updated: 4/8/2025, 11:09:10 pm
mod = 10 ** 9 + 7
N = 101
primes = [0] * N
primes[2] = 1
primes[3] = 1

def is_prime(num):
    if num % 2 == 0: return 0
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num != i and num % i == 0: return 0
    return 1

for num in range(4, N):
    primes[num] = is_prime(num)

fact = [1] * N
for i in range(1, N):
    fact[i] = fact[i - 1] * i % mod

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = 0
        non_prime = 0
        for i in range(1, n + 1):
            if primes[i]:
                prime += 1
            else:
                non_prime += 1
        # print(prime, non_prime)
        return fact[prime] * fact[non_prime] % mod