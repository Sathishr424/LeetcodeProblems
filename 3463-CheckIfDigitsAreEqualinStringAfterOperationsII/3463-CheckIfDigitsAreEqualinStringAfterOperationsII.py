# Last updated: 24/10/2025, 5:27:40 am
fact = [1] * 5
for i in range(1, 5):
    fact[i] = i * fact[i-1]

@cache
def ncr(n, k):
    return fact[n] // (fact[k] * fact[n - k])

def getCoeffForPrime(n, k, p):
    ans = 1
    while n and k:
        x = n % p
        y = k % p
        if x < y: return 0
        ans *= ncr(x, y)
        ans %= p

        n //= p
        k //= p
    
    return ans

remainder = [[0] * 5 for _ in range(2)]
for i in range(2):
    for j in range(5):
        for k in range(10):
            if k % 2 == i and k % 5 == j:
                remainder[i][j] = k

def getCoeff(n, k):
    coeff2 = getCoeffForPrime(n, k, 2)
    coeff5 = getCoeffForPrime(n, k, 5)

    return remainder[coeff2][coeff5]

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # 34789
        # 14641
        n = len(s)
        row = n-2

        left = 0
        right = 0
        for i in range(n-1):
            coeff = getCoeff(row, i)
            left += coeff * int(s[i]) % 10
            right += coeff * int(s[i + 1]) % 10
            left %= 10
            right %= 10
        
        return left == right