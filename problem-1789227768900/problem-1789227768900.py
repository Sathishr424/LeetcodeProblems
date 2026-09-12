# Last updated: 9/12/2026, 9:12:48 PM
1class Solution:
2    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
3        n = len(nums)
4        if k == 0: return n * (n + 1) // 2
5
6        sl = SortedList()
7        tot = 0
8        for i in range(n):
9            tot += nums[i]
10            sl.add(tot)
11
12        # x - y >= k
13        # x - 4 >= 2
14        ans = 0
15        tot = 0
16        for i in range(n):
17            index = sl.bisect_left(goal + k + tot)
18            window = len(sl) - index
19            ans += window
20
21            index = sl.bisect_left(goal - k + tot + 1)
22            ans += index
23
24            tot += nums[i]
25            sl.remove(tot)
26
27        return ans