# Last updated: 10/14/2026, 7:15:05 PM
1class Solution:
2    def resilientSubarray(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4
5        nums = [num % k for num in nums]
6    
7        best = 0
8        for i in range(n):
9            tot = 0
10            there = defaultdict(int)
11            for j in range(i, n):
12                tot += nums[j]
13                rem = tot % k
14                there[nums[j] % k] += 1
15
16                window = j - i + 1
17                if there[rem] == window:
18                    best = max(window, best)
19
20        return best