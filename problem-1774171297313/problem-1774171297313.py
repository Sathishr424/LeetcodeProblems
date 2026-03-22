# Last updated: 3/22/2026, 2:51:37 PM
1from typing import List
2from functools import cache
3
4class Solution:
5    def minRemovals(self, nums: List[int], target: int) -> int:
6        n = len(nums)
7
8        @cache
9        def rec(index, mask):
10            if index == n:
11                if mask == target: return 0
12                return inf
13            
14            return min(rec(index + 1, mask) + 1, rec(index + 1, mask ^ nums[index]))
15        
16        ans = rec(0, 0)
17        rec.cache_clear()
18        return -1 if ans == inf else ans