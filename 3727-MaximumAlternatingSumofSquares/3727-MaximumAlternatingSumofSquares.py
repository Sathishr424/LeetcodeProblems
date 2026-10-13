# Last updated: 10/13/2026, 5:53:39 PM
1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        n = len(nums)
4        nums = sorted([num * num for num in nums])
5
6        l = 0
7        r = n-1
8
9        ans = 0
10        for i in range(n//2):
11            ans += nums[r]
12            ans -= nums[l]
13            r -= 1
14            l += 1
15
16        if r == l:
17            ans += nums[r]
18
19        return ans