# Last updated: 10/19/2026, 10:51:29 AM
1class Solution:
2    def targetIndices(self, nums: list[int], target: int) -> list[int]:
3        less = 0
4        equal = 0
5
6        ret = []
7        for num in nums:
8            if num < target:
9                less += 1
10            elif num == target:
11                equal += 1
12
13        for i in range(equal):
14            ret.append(less + i)
15
16        return ret