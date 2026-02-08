# Last updated: 2/8/2026, 11:49:32 AM
1class Solution:
2    def dominantIndices(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        cnt = 0
6        right = nums[n-1]
7        for i in range(n-2, -1, -1):
8            av = right / (n - i - 1)
9            if nums[i] > av:
10                cnt += 1
11            right += nums[i]
12
13        return cnt
14            