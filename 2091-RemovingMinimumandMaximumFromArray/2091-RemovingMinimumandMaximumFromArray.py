# Last updated: 8/30/2026, 2:47:06 PM
1class Solution:
2    def minimumDeletions(self, nums: List[int]) -> int:
3        n = len(nums)
4        mn = min(nums)
5        mx = max(nums)
6
7        mn_index = 0
8        mx_index = 0
9        for i in range(n):
10            if nums[i] == mn:
11                mn_index = i
12            elif nums[i] == mx:
13                mx_index = i
14
15        if mn_index > mx_index:
16            mn_index, mx_index = mx_index, mn_index
17
18        return min(mx_index + 1, n - mn_index, mn_index + 1 + (n - mx_index))