# Last updated: 8/10/2026, 1:51:15 PM
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
16                if alice:
17                    if rec(rem - num, False): return True
18                else:
19                    if not rec(rem - num, True): return False
20
21            return not alice
22
23
24        ans = rec(n, True)
25        rec.cache_clear()
26
27        return ans
28