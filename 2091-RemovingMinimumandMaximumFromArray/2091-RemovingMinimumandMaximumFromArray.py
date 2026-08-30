# Last updated: 8/30/2026, 2:49:03 PM
1class Solution:
2    def minimumDeletions(self, nums: List[int]) -> int:
3        n = len(nums)
4        mn = nums[0]
5        mx = nums[0]
6        mn_index = 0
7        mx_index = 0
8
9        for i in range(n):
10            if nums[i] > mx:
11                mx = nums[i]
12                mx_index = i
13            elif nums[i] < mn:
14                mn = nums[i]
15                mn_index = i
16
17        if mn_index > mx_index:
18            mn_index, mx_index = mx_index, mn_index
19
20        return min(mx_index + 1, n - mn_index, mn_index + 1 + (n - mx_index))