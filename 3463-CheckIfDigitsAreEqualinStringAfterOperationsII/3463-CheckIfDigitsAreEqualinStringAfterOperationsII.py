# Last updated: 23/5/2025, 6:37:18 pm
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)

        def lucas(row, col):
            p_5 = getCoeff(row, col, 5)
            p_2 = getCoeff(row, col, 2)

            for i in range(10):
                if i % 5 == p_5 and i % 2 == p_2:
                    return i

        def getCoeff(row, col, mod):
            ans = 1
            while row and col:
                r = row % mod
                c = col % mod
                if r < c: return 0
                ans *= factorial(r) // (factorial(c) * factorial(r - c))
     
                ans %= mod
                row //= mod
                col //= mod
            
            return ans

        row = n-2
        left = int(s[0])
        right = int(s[-1])

        for col in range(1, n-1):
            e = lucas(row, col)
            left = (left + int(s[col]) * e % 10) % 10
            right = (right + int(s[n - col - 1]) * e % 10) % 10

        return left == right