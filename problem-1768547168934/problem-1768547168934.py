# Last updated: 1/16/2026, 12:36:08 PM
1class Solution:
2    def centeredSubarrays(self, nums: List[int]) -> int:
3        n = len(nums)
4        ret = 0
5        
6        for i in range(n):
7            s = 0
8            there = set()
9            for j in range(i, n):
10                s += nums[j]
11                there.add(nums[j])
12                if s in there: ret += 1
13
14        return ret