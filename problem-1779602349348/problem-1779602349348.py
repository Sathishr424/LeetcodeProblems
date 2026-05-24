# Last updated: 5/24/2026, 11:29:09 AM
1class Solution:
2    def minimumSwaps(self, nums: list[int]) -> int:
3        l = 0
4        r = len(nums) - 1
5
6        cost = 0
7        while l < r:
8            if nums[l] == 0:
9                while r > l and nums[r] == 0:
10                    r -= 1
11                if r > l:
12                    nums[l], nums[r] = nums[r], nums[l]
13                    cost += 1
14            l += 1
15
16        return cost