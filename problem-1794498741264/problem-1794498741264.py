# Last updated: 11/12/2026, 9:22:21 PM
1class Solution:
2    def minRotations(self, n: int, s: str) -> int:
3        nums = [int(num) for num in s]
4        best = 0
5        curr = 0
6        # Without rotating
7        for num in nums:
8            best += min((num - curr) % 10, (curr - num) % 10)
9            curr = num
10
11        # Building suffix array for ever reverse rotation on array at that index
12        suffix = [0] * n
13        last_num = nums[-1]
14
15        curr = nums[-1]
16        tot = 0
17        for i in range(n-2, -1, -1):
18            tot += min((nums[i] - curr) % 10, (curr - nums[i]) % 10)
19            curr = nums[i]
20            suffix[i] = tot
21
22        # Full rotation
23        best = min(best, tot + min(last_num,  10 - last_num))
24
25        # Calcualting prefix + suffix of the rotation at that index
26        tot = 0
27        curr = 0
28        for i in range(n-1):
29            tot += min((nums[i] - curr) % 10, (curr - nums[i]) % 10)
30            curr = nums[i]
31
32            suf = suffix[i+1]
33            rotated = min((last_num - curr) % 10, (curr - last_num) % 10)
34            best = min(best, suf + tot + rotated)
35
36        return best