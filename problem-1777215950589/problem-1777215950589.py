# Last updated: 4/26/2026, 8:35:50 PM
1class Solution:
2    def compareBitonicSums(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        index = 0
6        while index + 1 < n and nums[index] < nums[index + 1]:
7            index += 1
8
9        left = 0
10        for i in range(index+1):
11            left += nums[i]
12
13        right = 0
14        for i in range(index, n):
15            right += nums[i]
16
17        if left > right: return 0
18        elif left < right: return 1
19        return -1
20