# Last updated: 11/24/2026, 7:27:36 PM
1class Solution:
2    def minCost(self, nums: list[int]) -> int:
3        n = len(nums)
4        ans = nums[0] + nums[n-1]
5
6        negative_sum = 0
7        negative_cnt = 0
8        mn = inf
9        mx = -inf
10        for i in range(1, n-1):
11            if nums[i] < 0: 
12                negative_sum += nums[i]
13                negative_cnt += 1
14                mx = max(nums[i], mx)
15            else:
16                mn = min(mn, nums[i])
17
18        ans += negative_sum
19        # print(ans, mn, mx, (negative_cnt, negative_sum))
20        if negative_cnt & 1:
21            return min(ans + mn, ans - mx)
22        return ans