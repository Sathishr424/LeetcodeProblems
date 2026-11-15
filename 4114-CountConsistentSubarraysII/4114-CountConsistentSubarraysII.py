# Last updated: 11/15/2026, 11:42:47 PM
1class Solution:
2    def countConsistent(self, nums: list[int]) -> int:
3        n = len(nums)
4        ans = 0
5
6        LEFT = [0] * n
7        RIGHT = [n - 1] * n
8        for b in range(20):
9            i = 0
10            bit = 1 << b
11            while i < n:
12                start = i
13                while i < n and nums[i] & bit:
14                    i += 1
15                end = i - 1
16
17                j = i - 1
18                while j >= start:
19                    LEFT[j] = max(LEFT[j], start)
20                    RIGHT[j] = min(RIGHT[j], end)
21                    j -= 1
22
23                i = max(i + 1, i)
24
25        prevs = {}
26        getPrev = lambda x: prevs.get(x, 0)
27        for i in range(n):
28            left = LEFT[i]
29            right = RIGHT[i]
30
31            l = i - max(left, getPrev(nums[i])) + 1
32            r = right - i + 1
33            if right > i:
34                prevs[nums[i]] = i + 1
35            ans += l * r
36
37        return ans