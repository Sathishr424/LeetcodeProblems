# Last updated: 10/25/2026, 11:44:50 PM
1class Solution:
2    def countStaircase(self, nums: list[int]) -> int:
3        n = len(nums)
4
5        ans = 0
6        for i in range(n):
7            freq = defaultdict(int)
8            needed = defaultdict(int)
9            done = 0
10            k = 0
11            for j in range(i, n):
12                num = nums[j]
13                freq[num] += 1
14
15                if freq[num] == 1:
16                    k += 1
17                    needed[num] = k
18
19                if freq[num] == needed[num]:
20                    done += 1
21                    if done == k: ans += 1
22                elif freq[num] > needed[num]: 
23                    break
24
25        return ans