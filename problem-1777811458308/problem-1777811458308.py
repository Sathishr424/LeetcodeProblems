# Last updated: 5/3/2026, 6:00:58 PM
1class Solution:
2    def findValidElements(self, nums: list[int]) -> list[int]:
3        n = len(nums)
4
5        curr = nums[0]
6        min_p = []
7        min_s = [inf] * n
8        for i in range(n):
9            curr = max(curr, nums[i])
10            min_p.append(curr)
11
12        curr = nums[-1]
13        for i in range(n-1, -1, -1):
14            curr = max(curr, nums[i])
15            min_s[i] = curr
16
17
18
19        ans = []
20        for i in range(n):
21            if i == 0 or i == n-1 or min_p[i-1] < nums[i] or min_s[i+1] < nums[i]:
22                ans.append(nums[i])
23        
24        return ans
25
26