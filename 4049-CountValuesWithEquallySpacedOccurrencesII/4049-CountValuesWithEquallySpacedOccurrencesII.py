# Last updated: 9/12/2026, 11:01:07 PM
1class Solution:
2    def countSpecialIntegers(self, nums: list[int]) -> int:
3        indexes = defaultdict(list)
4        ans = 0
5
6        for i, num in enumerate(nums):
7            indexes[num].append(i)
8
9        for num in indexes:
10            if len(indexes[num]) < 3: continue
11
12            m = len(indexes[num])
13            ind = indexes[num]
14            diff = ind[1] - ind[0]
15
16            for i in range(2, m):
17                if ind[i] - ind[i - 1] != diff: break
18            else:
19                ans += 1
20
21        return ans