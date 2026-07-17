# Last updated: 7/18/2026, 1:58:49 AM
1class Solution:
2    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
3        m = max(nums)
4        cnt = [0] * (m + 1)
5        for num in nums:
6            cnt[num] += 1
7        for i in range(1, m + 1):
8            for j in range(i * 2, m + 1, i):
9                cnt[i] += cnt[j]
10        for i in range(1, m + 1):
11            cnt[i] = cnt[i] * (cnt[i] - 1) // 2
12        for i in range(m, 0, -1):
13            for j in range(i * 2, m + 1, i):
14                cnt[i] -= cnt[j]
15        for i in range(1, m + 1):
16            cnt[i] += cnt[i - 1]
17        ans = []
18        for q in queries:
19            q += 1
20            pos = bisect_left(cnt, q)
21            ans.append(pos)
22        return ans