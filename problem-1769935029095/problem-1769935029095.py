# Last updated: 2/1/2026, 2:07:09 PM
1class Solution:
2    def longestAlternating(self, nums: List[int]) -> int:
3        n = len(nums)
4        increasing = [0] * n
5        decreasing = [0] * n
6        increasingReverse = [0] * n
7        decreasingReverse = [0] * n
8
9        for i in range(1, n):
10            if nums[i] > nums[i-1]:
11                increasing[i] = decreasing[i-1] + 1;
12            elif nums[i] < nums[i-1]:
13                decreasing[i] = increasing[i-1] + 1;
14
15        for i in range(n-2, -1, -1):
16            if nums[i] > nums[i+1]:
17                decreasingReverse[i] = increasingReverse[i+1] + 1;
18            elif nums[i] < nums[i+1]:
19                increasingReverse[i] = decreasingReverse[i+1] + 1;
20
21        best = max(max(increasing), max(decreasing)) + 1
22        # print(increasing)
23        # print(decreasing)
24        # print(increasingReverse)
25        # print(decreasingReverse)
26        
27        for i in range(1, n-1):
28            if nums[i + 1] > nums[i-1]:
29                best = max(best, decreasing[i-1] + decreasingReverse[i+1] + 2)
30            elif nums[i + 1] < nums[i-1]:
31                best = max(best, increasing[i-1] + increasingReverse[i+1] + 2)
32            
33        return best