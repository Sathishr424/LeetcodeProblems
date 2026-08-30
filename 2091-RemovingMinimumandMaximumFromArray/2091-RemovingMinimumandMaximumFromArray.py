# Last updated: 8/30/2026, 2:41:44 PM
1class Solution:
2    def minimumDeletions(self, nums: List[int]) -> int:
3        n = len(nums)
4        mn = min(nums)
5        mx = max(nums)
6
7        cnt = 0
8        best = n
9        for i in range(n):
10            if nums[i] == mn or nums[i] == mx:
11                if cnt == 1:
12                    best = min(best, i + 1)
13                    break
14                cnt += 1
15
16        cnt = 0
17        for i in range(n-1, -1, -1):
18            if nums[i] == mn or nums[i] == mx:
19                if cnt == 1:
20                    best = min(best, n - i)
21                    break
22                cnt += 1
23
24        l = 0
25        while l < n and (nums[l] != mn and nums[l] != mx):
26            l += 1
27        r = n-1
28        while r >= 0 and (nums[r] != mn and nums[r] != mx):
29            r -= 1
30
31        best = min(best, l + 1 + (n - r))
32        return best