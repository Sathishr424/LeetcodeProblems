# Last updated: 22/12/2025, 3:45:59 pm
1class Solution:
2    def minDeletionSize(self, st: List[str]) -> int:
3        n = len(st)
4        m = len(st[0])
5
6        @cache
7        def rec(index, prev_index, prev_prev_index):
8            if index == m: return 0
9            
10            ans = rec(index + 1, prev_index, prev_prev_index) + 1
11            for i in range(n):
12                if st[i][index] < st[i][prev_index]:
13                    if prev_prev_index != -1:
14                        for i2 in range(n):
15                            if st[i2][index] < st[i2][prev_prev_index]:
16                                return ans
17                    return min(ans, rec(index + 1, index, prev_prev_index) + 1)
18            
19            return min(ans, rec(index + 1, index, prev_index))
20        
21        ans = rec(1, 0, -1)
22        rec.cache_clear()
23        return ans