# Last updated: 23/5/2025, 7:46:45 pm
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
            left = []
            right = []
            while row:
                left.append(row % mod)
                row //= mod
            while col:
                right.append(col % mod)
                col //= mod
            i = 0
            m = min(len(left), len(right))
            while i < m:
                r = left[i]
                c = right[i]
                if r < c: return 0
                ans *= factorial(r) // (factorial(c) * factorial(r - c))
     
                ans %= mod
                row //= mod
                col //= mod
                i += 1
            
            return ans

        row = n-2
        left = int(s[0])
        right = int(s[-1])

        for col in range(1, n-1):
            e = lucas(row, col)
            left = (left + int(s[col]) * e % 10) % 10
            right = (right + int(s[n - col - 1]) * e % 10) % 10

        return left == right