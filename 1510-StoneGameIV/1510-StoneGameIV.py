# Last updated: 8/10/2026, 1:53:47 PM
1squares = []
2num = 1
3N = 10**5
4while num * num <= N:
5    squares.append(num * num)
6    num += 1
7
8@cache
9def rec(rem, alice):
10    if rem == 0: return not alice
11
12    for num in squares:
13        if num > rem: break
14        if rec(rem - num, not alice) == alice: return alice
15
16    return not alice
17
18class Solution:
19    def winnerSquareGame(self, n: int) -> bool:
20        return rec(n, True)
21