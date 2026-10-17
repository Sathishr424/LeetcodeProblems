# Last updated: 10/17/2026, 10:26:14 PM
1class Solution:
2    def minSwaps(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        sorted_arr = []
6        for i, num in enumerate(nums):
7            s = 0
8            while num:
9                s += num % 10
10                num //= 10
11            sorted_arr.append((s, nums[i], i))
12
13        sorted_arr.sort()
14        indexes = [0] * n
15        for i in range(n):
16            indexes[i] = sorted_arr[i][2]
17
18        i = 0
19        ans = 0
20        while i < n:
21            if indexes[i] != i:
22                j = indexes[i]
23                indexes[i] = indexes[j]
24                indexes[j] = j
25                ans += 1
26            else:
27                i += 1
28
29        return ans