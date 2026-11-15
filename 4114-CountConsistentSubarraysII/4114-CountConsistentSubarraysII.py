# Last updated: 11/15/2026, 11:35:22 PM
1class Solution:
2    def countConsistent(self, nums: list[int]) -> int:
3        n = len(nums)
4        m = 20
5        ans = 0
6
7        LEFT = [0] * n
8        RIGHT = [n - 1] * n
9        for b in range(m):
10            i = 0
11            while i < n:
12                start = i
13                while i < n and nums[i] & (1 << b):
14                    i += 1
15
16                j = i - 1
17                while j >= start:
18                    LEFT[j] = max(LEFT[j], start)
19                    RIGHT[j] = min(RIGHT[j], i - 1)
20                    j -= 1
21
22                i = max(i + 1, i)
23
24        prevs = defaultdict(int)
25        for i in range(n):
26            left = LEFT[i]
27            right = RIGHT[i]
28
29            l = i - max(left, prevs[nums[i]]) + 1
30            r = right - i + 1
31            if right > i:
32                prevs[nums[i]] = i + 1
33            ans += l * r
34
35        return ans