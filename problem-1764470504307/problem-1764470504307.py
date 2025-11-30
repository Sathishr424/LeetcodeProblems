# Last updated: 30/11/2025, 8:11:44 am
1class Solution:
2    def minMirrorPairDistance(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        revs = defaultdict(list)
6        for i, num in enumerate(nums):
7            rev = 0
8            while num:
9                rem = num % 10
10                rev = rev * 10 + rem
11                num //= 10
12        
13            revs[rev].append(i)
14
15        best = 10**20
16        for i in range(n-1, -1, -1):
17            num = nums[i]
18            while revs[num] and revs[num][-1] >= i:
19                revs[num].pop()
20
21            if revs[num]:
22                best = min(best, i - revs[num][-1])
23
24        return -1 if best >= n else best