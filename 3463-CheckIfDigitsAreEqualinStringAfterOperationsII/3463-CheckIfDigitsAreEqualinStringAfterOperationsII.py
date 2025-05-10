# Last updated: 10/5/2025, 7:21:10 pm
fact = [1] * 6

for i in range(1, 6):
    fact[i] = i * fact[i-1]

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        dp = [int(i) for i in s]

        left = dp[0] + dp[-2]
        right = dp[1] + dp[-1]

        row = n-2

        def lucasMod(x, y, mod):
            a = 1
            while x and y:
                rem_x = x % mod
                rem_y = y % mod

                b = fact[rem_x] // (fact[rem_y] * fact[rem_x - rem_y]) % mod
                a = a * b % mod

                x //= mod
                y //= mod

            return a
        
        def helper(r, c):
            l2 = lucasMod(r, c, 2)
            l5 = lucasMod(r, c, 5)

            for i in range(10):
                if i % 2 == l2 and i % 5 == l5: return i

        for col in range(1, row):
            coeff = helper(row, col)

            left = (left + dp[col] * coeff) % 10
            right = (right + dp[n-col-1] * coeff) % 10

        return left == right