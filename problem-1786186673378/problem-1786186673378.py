# Last updated: 8/8/2026, 4:27:53 PM
1class Solution:
2    def minimumCost(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4        mod = 10**9 + 7
5
6        op = 0
7        rem = k
8
9        for i, num in enumerate(nums):
10            need = max(0, num - rem)
11            needed_op = (need + k - 1) // k
12            
13            op += needed_op
14            rem = rem + needed_op * k
15            
16            rem -= num
17
18        return op * (op + 1) // 2 % mod