# Last updated: 10/5/2025, 10:47:18 pm
fact = [1] * 6

for i in range(1, 6):
    fact[i] = i * fact[i-1]

pre = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        for k in range(10):
            if k % 2 == i and k % 5 == j:
                pre[i][j] = k
                break

memo = [[[0] * 6 for _ in range(6)] for _ in range(6)]

for x in range(6):
    for y in range(6):
        for z in range(6):
            memo[x][y][z] = fact[x] // (fact[y] * fact[x-y])

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

                a = a * memo[rem_x][rem_y][rem_x - rem_y]

                x //= mod
                y //= mod

            return a % mod
        
        def getCoeff(r, c):
            l2 = lucasMod(r, c, 2)
            l5 = lucasMod(r, c, 5)

            return pre[l2][l5]

        for col in range(1, row):
            coeff = getCoeff(row, col)

            left = (left + dp[col] * coeff) % 10
            right = (right + dp[n-col-1] * coeff) % 10

        return left == right