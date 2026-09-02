# Last updated: 9/2/2026, 7:37:20 AM
1class Solution:
2    def uniformArray(self, nums: list[int]) -> bool:
3        odd = 0
4        for num in nums:
5            if num % 2:
6                odd += 1
7
8        # odd
9        for num in nums:
10            if num % 2 == 0:
11                if odd == 0: break
12        else:
13            return True
14
15        # even
16        for num in nums:
17            if num % 2:
18                if odd == 1: break
19        else:
20            return True
21
22        return False