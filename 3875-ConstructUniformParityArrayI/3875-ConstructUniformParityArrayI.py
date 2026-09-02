# Last updated: 9/2/2026, 7:36:32 AM
1class Solution:
2    def uniformArray(self, nums: list[int]) -> bool:
3        n = len(nums)
4
5        odd = 0
6        even = 0
7        for num in nums:
8            if num % 2:
9                odd += 1
10            else:
11                even += 1
12
13        # odd
14        for num in nums:
15            if num % 2 == 0:
16                if odd == 0: break
17        else:
18            return True
19
20        # even
21        for num in nums:
22            if num % 2:
23                if odd == 1: break
24        else:
25            return True
26
27        return False