# Last updated: 10/25/2026, 11:37:36 PM
1class Solution:
2    def maximizeSum(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4
5        new_arr = []
6        for i, num in enumerate(nums):
7            orig_num = num
8            digits = []
9            while num:
10                digits.append(num % 10)
11                num //= 10
12            digits.sort(reverse=True)
13            new_num = 0
14            for d in digits:
15                new_num = new_num * 10 + d
16            new_arr.append((new_num - orig_num, i, new_num))
17
18        new_arr.sort(reverse=True)
19        ans = 0
20        for i in range(k):
21            ans += new_arr[i][2]
22
23        for i in range(k, n):
24            ans += nums[new_arr[i][1]]
25
26        return ans