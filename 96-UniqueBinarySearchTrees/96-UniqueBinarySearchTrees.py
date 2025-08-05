# Last updated: 5/8/2025, 11:01:59 am
fact = [1] * 201
for i in range(1, 201):
    fact[i] = fact[i - 1] * i

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return fact[m + n - 2] // (fact[m - 1] * fact[n - 1])