# Last updated: 8/8/2026, 4:25:34 PM
1class Solution:
2    def minimumCost(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        mod = 10**9 + 7
5
6        op = 0
7        rem = k
8        cost = 0
9
10        for i, num in enumerate(nums):
11            need = max(0, num - rem)
12            needed_op = (need + k - 1) // k
13
14            cost += needed_op * op + (needed_op * (needed_op + 1) // 2)
15            cost %= mod
16
17            op += needed_op
18            rem = rem + needed_op * k
19
20            rem -= num
21
22        return cost