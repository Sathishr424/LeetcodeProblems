# Last updated: 5/24/2026, 12:03:05 PM
1class Solution:
2    def minOperations(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4
5        min_cost = inf
6        for x in range(k):
7            for y in range(k):
8                if x == y: continue
9                cost = 0
10                for i in range(n):
11                    rem = nums[i] % k
12                    if i % 2 == 0:
13                        need = abs(rem - x)
14                        cost += min(need, k - need)
15                    else:
16                        need = abs(rem - y)
17                        cost += min(need, k - need)
18                min_cost = min(min_cost, cost)
19                # print((x, y), cost)
20
21        return min_cost