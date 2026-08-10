# Last updated: 8/10/2026, 1:52:14 PM
1squares = []
2num = 1
3N = 10**5
4while num * num <= N:
5    squares.append(num * num)
6    num += 1
7class Solution:
8    def winnerSquareGame(self, n: int) -> bool:
9
10        @cache
11        def rec(rem, alice):
12            if rem == 0: return not alice
13
14            for num in squares:
15                if num > rem: break
16                if rec(rem - num, not alice) == alice: return alice
17
18            return not alice
19
20
21        ans = rec(n, True)
22        rec.cache_clear()
23
24        return ans