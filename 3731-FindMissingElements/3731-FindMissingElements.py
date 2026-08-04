# Last updated: 8/4/2026, 3:36:17 PM
1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4
5        mn = nums[0]
6        mx = nums[0]
7        there = set()
8
9        for num in nums:
10            if num < mn:
11                mn = num
12            if num > mx:
13                mx = num
14            there.add(num)
15
16        ret = []
17        for num in range(mn+1, mx):
18            if num not in there:
19                ret.append(num)
20
21        return ret