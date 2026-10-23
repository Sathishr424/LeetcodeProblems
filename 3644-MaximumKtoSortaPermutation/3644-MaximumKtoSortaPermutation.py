# Last updated: 10/23/2026, 3:58:00 PM
1class Solution:
2    def sortPermutation(self, nums: List[int]) -> int:
3        n = len(nums)
4        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
5        ans = -1
6        for i in range(n):
7            if sorted_nums[i][0] != nums[i]:
8                if ans == -1: ans = nums[i]
9                else: ans &= nums[i]
10        return max(0, ans)