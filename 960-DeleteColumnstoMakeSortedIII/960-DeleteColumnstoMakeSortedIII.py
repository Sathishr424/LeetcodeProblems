# Last updated: 22/12/2025, 3:48:14 pm
1class Solution:
2    def minDeletionSize(self, st: List[str]) -> int:
3        n = len(st)
4        m = len(st[0])
5
6        def isAllSmaller(index, prev_index):
7            for i in range(n):
8                if st[i][index] < st[i][prev_index]: return False
9            return True
10
11        @cache
12        def rec(index, prev_index, prev_prev_index):
13            if index == m: return 0
14            
15            ans = rec(index + 1, prev_index, prev_prev_index) + 1
16            for i in range(n):
17                if st[i][index] < st[i][prev_index]:
18                    if prev_prev_index != -1 and not isAllSmaller(index, prev_prev_index):
19                        return ans
20                    return min(ans, rec(index + 1, index, prev_prev_index) + 1)
21            
22            return min(ans, rec(index + 1, index, prev_index))
23        
24        ans = rec(1, 0, -1)
25        rec.cache_clear()
26        return ans