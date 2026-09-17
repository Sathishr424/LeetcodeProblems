# Last updated: 9/17/2026, 3:26:27 PM
1class Solution:
2    def minSumOfLengths(self, arr: List[int], target: int) -> int:
3        n = len(arr)
4        prefix = [0]
5        for num in arr:
6            prefix.append(prefix[-1] + num)
7
8        @cache
9        def rec(index, status):
10            if status == 2:
11                return 0
12            if index == n:
13                return inf
14
15            ans = rec(index + 1, status)
16            need = prefix[index] + target
17            right = bisect_left(prefix, need, lo=index + 1)
18            if right <= n and prefix[right] == need:
19                ans = min(ans, rec(right, status + 1) + (right - index))
20            return ans
21
22        ans = rec(0, 0)
23        rec.cache_clear()
24        return -1 if ans == inf else ans