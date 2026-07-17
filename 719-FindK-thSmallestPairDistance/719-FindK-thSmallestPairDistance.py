# Last updated: 7/17/2026, 4:06:46 PM
1class Solution:
2    def smallestDistancePair(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        nums.sort()
5
6        def getCnt(dis):
7            cnt = 0
8            for i in range(n):
9                cnt += bisect_right(nums, nums[i] + dis) - i - 1
10            return cnt
11
12        l = 0
13        r = nums[-1] - nums[0]
14
15        while l < r:
16            mid = (l + r) // 2
17
18            cnt = getCnt(mid)
19            # print(l, r, mid, cnt)
20
21            if cnt >= k:
22                r = mid
23            else:
24                l = mid + 1
25
26        return l