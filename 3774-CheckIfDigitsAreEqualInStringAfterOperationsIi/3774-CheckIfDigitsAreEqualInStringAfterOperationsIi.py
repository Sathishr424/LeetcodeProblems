# Last updated: 12/6/2025, 5:34:27 am
fact = [1] * 5
for i in range(1, 5):
    fact[i] = fact[i-1] * i

pre = [[0] * 10 for _ in range(10)]
for i in range(10):
    pre[i % 5][i % 2] = i

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)

        def lucas(row, col):
            p_5 = getCoeff(row, col, 5)
            p_2 = getCoeff(row, col, 2)

            return pre[p_5][p_2]

        def getCoeff(row, col, mod):
            ans = 1
            while row and col:
                r = row % mod
                c = col % mod
                if r < c: return 0
                ans *= fact[r] // (fact[c] * fact[r - c])
     
                ans %= mod
                row //= mod
                col //= mod
            
            return ans

        row = n-2
        left = 0
        right = 0

        for col in range(n-1):
            e = lucas(row, col)
            left = (left + int(s[col]) * e % 10) % 10
            right = (right + int(s[col+1]) * e % 10) % 10

        return left == right