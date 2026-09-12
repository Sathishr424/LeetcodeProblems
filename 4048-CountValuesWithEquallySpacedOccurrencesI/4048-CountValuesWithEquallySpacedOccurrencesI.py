# Last updated: 9/12/2026, 11:00:49 PM
1class Solution:
2    def countSpecialIntegers(self, nums: list[int]) -> int:
3        indexes = defaultdict(list)
4        ans = 0
5
6        for i, num in enumerate(nums):
7            indexes[num].append(i)
8
9        for num in indexes:
10            if len(indexes[num]) != 3: continue
11
12            i, j, k = indexes[num]
13
14            if j - i == k - j: ans += 1
15
16        return ans