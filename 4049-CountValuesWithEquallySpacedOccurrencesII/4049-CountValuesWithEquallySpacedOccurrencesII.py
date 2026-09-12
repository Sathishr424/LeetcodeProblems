# Last updated: 9/12/2026, 11:01:45 PM
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
14        #
15        # for i in range(n):
16        #     tot = 0
17        #     for j in range(i, n):
18        #         tot += nums[j]
19        #         print((i, j), nums[i:j+1], tot, abs(tot - goal) >= k)
20        
21        ans = 0
22        tot = 0
23        for i in range(n):
24            index = sl.bisect_left(goal + k + tot)
25            window = len(sl) - index
26            ans += window
27
28            index = sl.bisect_left(goal - k + tot + 1)
29            ans += index
30
31            tot += nums[i]
32            sl.remove(tot)
33
34        return ans