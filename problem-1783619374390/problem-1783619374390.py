# Last updated: 7/9/2026, 11:19:34 PM
1class Solution:
2    def countValidSubarrays(self, nums: list[int], x: int) -> int:
3        n = len(nums)
4        ans = 0
5
6        for i in range(n):
7            sum = 0
8            for j in range(i, n):
9                sum += nums[j]
10                if sum % 10 == x and int(str(sum)[0]) == x:
11                    ans += 1
12
13        return ans