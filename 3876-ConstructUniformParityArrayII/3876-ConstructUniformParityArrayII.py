# Last updated: 9/3/2026, 4:02:01 PM
1class Solution:
2    def uniformArray(self, nums: list[int]) -> bool:
3        nums = sorted(set(nums))
4
5        #odd
6        odd = 0
7        for num in nums:
8            if num % 2 == 0:
9                if odd == 0: break
10            else:
11                odd += 1
12        else:
13            return True
14
15        #even
16        odd = 0
17        for num in nums:
18            if num % 2:
19                if odd == 0: break
20                odd += 1
21        else:
22            return True
23
24        return False