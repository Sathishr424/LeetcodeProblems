# Last updated: 24/10/2025, 5:14:18 am
fact = [1] * 10
for i in range(1, 10):
    fact[i] = i * fact[i-1]

def ncrC(n, k, p):
    ans = 1
    while n and k:
        x = n % p
        y = k % p

        ans *= fact[x] // (fact[y] * fact[x - y])
        ans %= p

        n //= p
        k //= p
    
    return ans

def ncr(n, k):
    coeff2 = ncrC(n, k, 2)
    coeff5 = ncrC(n, k, 5)

    for i in range(10):
        if i % 2 == coeff2 and i % 5 == coeff5:
            return i

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # 34789
        # 14641
        n = len(s)
        row = n-2

        left = 0
        for i in range(n-1):
            left += ncr(row, i) * int(s[i])
            left %= 10
        
        right = 0
        for i in range(1, n):
            right += ncr(row, i - 1) * int(s[i])
            right %= 10
        
        # print(left, right)
        
        return left == right