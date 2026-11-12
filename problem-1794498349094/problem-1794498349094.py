# Last updated: 11/12/2026, 9:15:49 PM
1class Solution:
2    def minRotations(self, n: int, s: str) -> int:
3        nums = [int(num) for num in s]
4        suffix = [0] * n
5
6        curr = nums[-1]
7        tot = 0
8        for i in range(n-2, -1, -1):
9            tot += min((nums[i] - curr) % 10, (curr - nums[i]) % 10)
10            curr = nums[i]
11            suffix[i] = tot
12
13        last_num = nums[-1]
14
15        best = tot + min((last_num - 0) % 10, (0 - last_num) % 10)
16
17        tot = 0
18        curr = 0
19        for i in range(n-1):
20            tot += min((nums[i] - curr) % 10, (curr - nums[i]) % 10)
21
22            curr = nums[i]
23            suf = suffix[i+1]
24            rotated = min((last_num - curr) % 10, (curr - last_num) % 10)
25            best = min(best, suf + tot + rotated)
26
27        tot += min((last_num - curr) % 10, (curr - last_num) % 10)
28        best = min(best, tot)
29        return best