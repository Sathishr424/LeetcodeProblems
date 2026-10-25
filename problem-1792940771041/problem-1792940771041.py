# Last updated: 10/25/2026, 8:36:11 PM
1class Solution:
2    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
3        n = len(nums)
4
5        def do(index):
6            if index == n: return 0
7            left = index
8            while left < n and (nums[left] < minK or nums[left] > maxK):
9                left += 1
10
11            ans = 0
12            right = left
13            if right < n:
14                while right < n and nums[right] >= minK and nums[right] <= maxK:
15                    ans += right - left + 1
16                    right += 1
17
18            return ans + do(right)
19
20        return do(0)