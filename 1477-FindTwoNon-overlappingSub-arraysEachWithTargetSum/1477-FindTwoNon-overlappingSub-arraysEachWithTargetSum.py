# Last updated: 9/17/2026, 3:46:23 PM
1class Solution:
2    def minSumOfLengths(self, arr: List[int], target: int) -> int:
3        n = len(arr)
4
5        best = [inf] * (n + 2)
6        tot = 0
7        left = 0
8        ans = inf
9        for i in range(n):
10            tot += arr[i]
11            best[i] = min(best[i], best[i - 1])
12            while tot > target:
13                tot -= arr[left]
14                left += 1
15
16            if tot == target:
17                best[i] = min(i - left + 1, best[i])
18                ans = min(ans, (i - left + 1) + best[left - 1])
19
20        return -1 if ans == inf else ans