# Last updated: 11/24/2026, 6:21:53 PM
1class Solution:
2    def countDominantElements(self, nums: list[int]) -> int:
3        n = len(nums)
4        if n == 1: return 1
5        ans = 0
6
7        for i in range(1, n-1):
8            if (nums[i-1] + nums[i+1]) / 2 <= nums[i]: ans += 1
9
10        if n > 1 and nums[0] >= nums[1]: ans += 1
11        if n > 1 and nums[-1] >= nums[-2]: ans += 1
12        
13        return ans