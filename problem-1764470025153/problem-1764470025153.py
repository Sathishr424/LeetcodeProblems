# Last updated: 30/11/2025, 8:03:45 am
1class Solution:
2    def countElements(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        nums.sort()
5        ans = 0
6
7        for i in range(n):
8            index = bisect_right(nums, nums[i])
9            rem = n - index
10            if rem >= k: ans += 1
11
12        return ans
13            