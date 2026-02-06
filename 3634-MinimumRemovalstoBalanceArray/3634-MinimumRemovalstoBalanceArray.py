# Last updated: 2/7/2026, 1:20:19 AM
1class Solution:
2    def minRemoval(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4
5        nums.sort()
6        best = inf
7                
8        for i in range(n):
9            left = i
10            num = nums[i]
11
12            index = bisect_right(nums, num * k)
13
14            right = n - index
15
16            best = min(best, left + right)
17
18        return best